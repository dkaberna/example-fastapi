from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
 


router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), 
         current_user: models.User = Depends(oauth2.get_current_user)):
    
    # Logic to see if user is voting on a post that exists
    post_query = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with {vote.post_id} does not exist")


    # Checks if user has voted for this post
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, 
                                models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()

    if (vote.dir == 1):
        # Already found a vote, so raise exception
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        # Create a brand new vote
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        
        # Add to database
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
        
    else:
        if not found_vote:
            # Can't delete a vote that doesn't exist
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"vote does not exist")
        
        # Delete vote
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted vote"}