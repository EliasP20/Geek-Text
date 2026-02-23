from sqlalchemy.orm import Session
from app.models.user import User
from app.models.credit_card import CreditCard
from app.schemas.credit_card import CreditCardCreate

def create_credit_card_for_user(db: Session, username: str, data: CreditCardCreate) -> bool:
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False

    card = CreditCard(
        user_id=user.id,
        card_number=data.card_number,
        card_holder_name=data.card_holder_name,
        exp_month=data.exp_month,
        exp_year=data.exp_year,
    )

    db.add(card)
    db.commit()
    return True
