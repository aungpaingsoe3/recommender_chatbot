import re
import phone_plans


def delete_plans(plans, category, flag):
    """
    Deletes phone plans that are not suitable to the user

    :param plans: The remaining phone plans suitable to the user
    :param category: Unlimited Talk & Text or Unlimited Data
    :param flag: True or False value indicating user's desire
    :return: The dictionary that contains the remaining phone plans
    """
    to_delete = []
    for plan in plans:
        if plans[plan][category] != flag:
            to_delete.append(plan)
    for key in to_delete:
        del plans[key]
    return plans

def main():
    """
    The main function that runs the chatbot
    """
    all_plans = phone_plans.plans
    lines = 0
    print("Welcome to the Phone Plan Recommender!\nTo get started, please answer the following question below.")
    # Asking the number of phone lines the user wants
    while True:
        user_input = input("How many phone lines do you need? Or enter quit to exit the recommender.\n")
        # Case for quitting the chatbot conversation
        if re.match(r'^.*(quit|exit|bye).*$', user_input.lower()):
            print("Thank you for using the Phone Plan Selector! Hope you have a great day!")
            exit()
        # Capturing the number of phone lines the user wants
        elif re.match(r'^.*\d+.*$', user_input.lower()):
            lines = int(re.search(r'\d+', user_input).group())
            break
        # Special case when the user wants 1 line
        elif re.match(r'^.*\s(a|one)\s.*$', user_input.lower()):
            lines = 1
            break
        # Special case when the user wants no lines
        elif re.match(r'^.*(none|zero|no).*$', user_input.lower()):
            print("Thank you for using the Phone Plan Selector! Hope you have a great day!")
            exit()
        else:
            # Error Handling on when the user does not provide a number
            print("Sorry, I could not understand your response. Can you answer the following question again?")
            continue
    # Asking whether the user wants unlimited talk and text in the plan
    while True:
        user_input = input("Do you need unlimited talk and text in your plan? Or enter quit to exit the recommender.\n")
        # Case for quitting the chatbot conversation
        if re.match(r'^.*(quit|exit|bye).*$', user_input.lower()):
            print("Thank you for using the Phone Plan Selector! Hope you have a great day!")
            exit()
        # Case when the user doesn't want unlimited talk and text
        elif re.match(r"^.*(no|nope|do not|don't).*$", user_input.lower()):
            # Deletes all the plans in the potential phone plans that have unlimited talk and text
            unlimited_tt = False
            all_plans = delete_plans(all_plans, 'unlimited_talk_text', unlimited_tt)
            break
        # Case when the user wants unlimited talk and text
        elif re.match(r'^.*(yes|yea|do|need|want|sure).*$', user_input.lower()):
            # Deletes all the plans in the potential phone plans that does have unlimited talk and text
            unlimited_tt = True
            all_plans = delete_plans(all_plans, 'unlimited_talk_text', unlimited_tt)
            break
        else:
            # Error Handling on when the user does not provide a clear answer
            print("Sorry, I could not understand your response. Can you answer the following question again?")
            continue
    # Asking question on whether user wants unlimited data in the plan
    while True:
        user_input = input("Do you need unlimited data in your plan? Or enter quit to exit the recommender.\n")
        # Case for quitting the chatbot conversation
        if re.match(r'^.*(quit|exit|bye).*$', user_input.lower()):
            print("Thank you for using the Phone Plan Selector! Hope you have a great day!")
            exit()
        # Case when the user doesn't want unlimited data
        elif re.match(r"^.*(no|nope|do not|don't).*$", user_input.lower()):
            # Deletes all the plans in the potential phone plans that does have unlimited data
            unlimited_data = False
            all_plans = delete_plans(all_plans, 'unlimited_data', unlimited_data)
            break
        # Case when the user wants unlimited data
        elif re.match(r'^.*(yes|yea|do|need|want|sure).*$', user_input.lower()):
            # Deletes all the plans in the potential phone plans that does not have unlimited data
            unlimited_data = True
            all_plans = delete_plans(all_plans, 'unlimited_data', unlimited_data)
            break
        else:
            # Error Handling on when the user does not provide a clear answer
            print("Sorry, I could not understand your response. Can you answer the following question again?")
            continue

    # Final recommendation when the dictionary of potential phone plans only has a size of 1
    if len(all_plans) == 1:
        remaining_plan = list(all_plans.keys())[0]
        cost_per_line = all_plans[remaining_plan]['monthly_cost_per_line']
        recommendation = (f"Plan Name: {remaining_plan}\n"
                          f"Monthly Cost Per Line: ${cost_per_line}\n"
                          f"Number of Lines Requested: {lines}\n"
                          f"Total Monthly Cost: ${cost_per_line * lines}")
        print("After entering what you need, we would recommend the following plan:\n")
        print(recommendation, "\n")
        print("Note: This monthly price does not include taxes or fees.")
        print("Thank you for using the Phone Plan Recommender! Hope you have a great day!")


if __name__ == "__main__":
    main()
