from sqlalchemy import Date, ForeignKey, CheckConstraint, String
from sqlalchemy.orm import mapped_column, Mapped
from Enrollment import Enrollment

class LetterGrade(Enrollment):
    __tablename__ = "letter_grade"
    letterGradeId: Mapped[int] = mapped_column('letter_grade_id',
                                               ForeignKey("enrollments.enrollment_id",
                                                          ondelete="CASCADE"), primary_key=True)
    minSatisfactory: Mapped[str] = mapped_column('min_satisfactory', String,
                                                 CheckConstraint("min_satisfactory IN ('A', 'B', 'C', 'D', 'F')", name="letter_grade_min_satisfactory_constraint"),
                                                 nullable=False)
    __mapper_args__ = {"polymorphic_identity": "letter_grade"}

    def __init__(self, section, student, min_satisfactory):
        super().__init__(section, student)
        self.minSatisfactory = min_satisfactory

    def __str__(self):
        return f"LetterGrade Enrollment: {super().__str__()}"