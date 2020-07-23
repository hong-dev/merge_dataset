import pandas as pd

contact_data = pd.read_csv(
    "./dataset/CONTACT_HISTORY.csv",
    encoding="shift_jis",
    low_memory=False,
    header=0,
    names=["client_id", "contact_type", "contact_date"],
)
transfer_data = pd.read_csv(
    "./dataset/IDOU_DATA_ALL.csv",
    encoding="shift_jis",
    header=0,
    names=[
        "policy_no",
        "insurance_start_date",
        "insurance_end_date",
        "transfer_date_8_digit",
        "transfer_date",
        "effectiveness_end_date",
        "transfer_reason_1",
        "transfer_reason_2",
        "transfer_reason_3",
        "transfer_reason_4",
        "transfer_reason_5",
        "collected_returned_premium",
        "transfer_route",
        "reception_route",
        "actual_transfer_date",
    ],
)
policy_data = pd.read_csv(
    "./dataset/POLICY.csv",
    encoding="shift_jis",
    header=0,
    names=[
        "client_id",
        "subscriber_id",
        "application_no",
        "policy_no",
        "previous_policy_no",
        "insurance_start_date",
        "city",
        "gender",
        "birth_date",
        "age",
        "mail_address",
        "underwriting_restriction",
        "grade",
        "renewal_no",
        "initial_registration_date",
        "car_age",
        "internet_related_contract",
        "annual_premium",
        "paperless",
        "personal_class",
        "property_class",
        "automobile_class",
        "vehicle_type",
        "vehicle_price_lower",
        "vehicle_price_upper",
        "driver_restriction",
        "age_condition",
        "contract_distance",
        "3_rank_downgraded",
        "accidents_grading_maintained",
        "no_count_accident",
        "renewal_code",
        "property_damage_liability_restriction",
        "bodily_injured",
        "price_for_human_injury",
        "injury",
        "price_for_passenger_injury",
        "automobile_insurance",
        "accidents_getting_out_of_the_cars",
        "attorney_cost",
        "FB_option",
        "gold_grade_driver's_license",
        "insured_relationship_with_the_contractor",
        "insured_birth_date",
        "registered_age",
        "department_code",
        "multiple_contract_discount",
        "introduction",
        "appropriation_date",
        "MGM",
        "accident",
        "RS",
    ],
)
policy_last_data = pd.read_csv(
    "./dataset/POLICY_LAST_YEAR.csv",
    encoding="shift_jis",
    header=0,
    names=[
        "client_id",
        "subscriber_id",
        "application_no",
        "policy_no",
        "previous_policy_no",
        "insurance_start_date",
        "city",
        "gender",
        "birth_date",
        "age",
        "mail_address",
        "underwriting_restriction",
        "grade",
        "renewal_no",
        "initial_registration_date",
        "car_age",
        "internet_related_contract",
        "annual_premium",
        "paperless",
        "personal_class",
        "property_class",
        "automobile_class",
        "vehicle_type",
        "vehicle_price_lower",
        "vehicle_price_upper",
        "driver_restriction",
        "age_condition",
        "contract_distance",
        "3_rank_downgraded",
        "accidents_grading_maintained",
        "no_count_accident",
        "renewal_code",
        "property_damage_liability_restriction",
        "bodily_injured",
        "price_for_human_injury",
        "injury",
        "price_for_passenger_injury",
        "automobile_insurance",
        "accidents_getting_out_of_the_cars",
        "attorney_cost",
        "FB_option",
        "gold_grade_driver's_license",
        "insured_relationship_with_the_contractor",
        "insured_birth_date",
        "registered_age",
        "department_code",
        "multiple_contract_discount",
        "introduction",
        "appropriation_date",
        "MGM",
        "accident",
        "RS",
    ],
)

policy_two_years = pd.merge(
    policy_data,
    policy_last_data,
    how="outer",
    left_on=["previous_policy_no", "client_id"],
    right_on=["policy_no", "client_id"],
)

print(policy_data)

# print(contact_data)
#
# policy_two_years.to_csv("policy_two_years.csv")
# contact_data.to_csv("contact.csv")
# policy_data.to_csv("policy.csv")
# policy_last_data.to_csv("policy_last.csv")
# transfer_data.to_csv("transfer.csv")

policy_last_idou = pd.merge(
    policy_last_data,
    transfer_data,
    how="outer",
    on="policy_no"
)

policy_idou = pd.merge(
    policy_data,
    transfer_data,
    how="outer",
    on="policy_no"
)

policy_last_idou.to_csv("policy_last_idou.csv", index=False, encoding='utf-8')
policy_idou.to_csv("policy_idou.csv", index=False, encoding='utf-8')