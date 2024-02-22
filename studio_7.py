import csv


class Participant:
    def __init__(self, age, industry, salary, currency, country, experience, education):
        # self.x = x
        self.age = age
        self.industry = industry
        self.salary = salary
        self.currency = currency
        self.country = country
        self.experience = experience
        self.education = education

# TODO: Create a AverageSalary class
    # Including:
    # key - this is the group key (i.e. "Accounting, Banking & Finance" from industry)
    # average - this is the average salary
    # participant count - this is how many total participants fit into this group

def main():
    print("hello world")
    rows = load_csv_file("survey.csv")
    participants = create_participants(rows)

    print("Answer #1:", len(participants))

    industry_groups = group_by_attribute(participants, "industry")

    average_salaries_by_industry = get_average_salary(industry_groups)
    
    # TODO: print top 5 industries by salary. Only include industries with at least 10 participants

    # TODO: Use existing logic to solve questions 3,4,5

    return


def get_average_salary(groups_list):
    average_salaries = []
    for key, group in groups_list.items():
        avg = int(sum([x.salary for x in group]) / len(group))
        # TODO: With the AverageSalaries class we created, append in instance of AverageSalaries instead of just key, avg, len(group)
        average_salaries.append((key, avg, len(group)))

    return average_salaries

def group_by_attribute(objects, property):
    # The logic for groupping has been simplified greatly for both faster execution and easier understanding
    
    groups = {}
    
    # create a dictionary using the property
    for obj in objects:
        value = getattr(obj, property)
        if value in groups:
            groups[value].append(obj)
        else:
            groups[value] = [obj]

    return groups




def create_participants(rows):
    # Age, Industry, Salary, Currency, Country, Years of Experience Overall, Highest level of Education

    participants = []

    for row in rows[1:]:
        age = row[1]
        industry = row[2]
        salary = int(row[5].replace(",",""))
        currency = row[7]
        country = row[10]
        experience = row[13]
        education = row[15]
        # only add if currency == 'USD'
        if currency == "USD":
            participants.append(Participant(age, industry, salary, currency, country, experience, education))

    return participants



def load_csv_file(filename):
    rows = []
    with open(filename, "r", encoding='iso-8859-1') as f:
        reader_obj = csv.reader(f)

        for row in reader_obj:
            rows.append(row)

    return rows

if __name__ == "__main__":
    main()