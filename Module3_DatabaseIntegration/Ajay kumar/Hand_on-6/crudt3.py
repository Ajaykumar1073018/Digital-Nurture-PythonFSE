# =====================================================
# TASK 3
# N+1 PROBLEM
# =====================================================

print("\n========== WITHOUT joinedload() ==========\n")

enrollments = session.query(
    Enrollment
).all()

for enrollment in enrollments:

    print(

        enrollment.student.first_name,

        "-",

        enrollment.course.course_name

    )


print("\nObserve SQL logs above.")
print("Many SQL statements executed.")


# =====================================================
# USING joinedload()
# =====================================================

print("\n========== WITH joinedload() ==========\n")

enrollments = (

    session.query(Enrollment)

    .options(

        joinedload(Enrollment.student),

        joinedload(Enrollment.course)

    )

    .all()

)

for enrollment in enrollments:

    print(

        enrollment.student.first_name,

        "-",

        enrollment.course.course_name,

        "-",

        enrollment.grade

    )


print("\nOnly ONE SQL query executed using JOIN.")


# =====================================================

session.close()

print("\nProgram Completed Successfully.")
