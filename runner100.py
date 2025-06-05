import random

def generate_athlete_data(num_athletes):
    names = [
        "John Smith", "Jane Doe", "Michael Johnson", "Emily Davis", "Chris Brown",
        "Jessica Wilson", "David Lee", "Sarah Miller", "James Taylor", "Laura Anderson",
        "Daniel Thomas", "Sophia Martinez", "Matthew Jackson", "Olivia White", "Joshua Harris",
        "Mia Clark", "Ethan Lewis", "Ava Robinson", "Alexander Walker", "Isabella Hall",
        "Liam Young", "Charlotte Allen", "Noah King", "Amelia Wright", "Lucas Scott",
        "Harper Green", "Benjamin Adams", "Ella Baker", "Jacob Nelson", "Grace Carter",
        "William Mitchell", "Chloe Perez", "Michael Roberts", "Sofia Turner", "Elijah Phillips",
        "Zoe Campbell", "Jameson Parker", "Lily Evans", "Jackson Edwards", "Aria Edwards",
        "Aiden Collins", "Scarlett Stewart", "Gabriel Sanchez", "Victoria Morris", "Samuel Rivera",
        "Madison Cooper", "Henry Reed", "Avery Morgan", "Owen Bell", "Samantha Murphy"
    ]
    
    countries = [
        "USA", "Canada", "UK", "Australia", "Germany",
        "France", "Italy", "Spain", "Japan", "China",
        "Brazil", "India", "South Africa", "Russia", "Mexico",
        "Netherlands", "Sweden", "Norway", "Finland", "New Zealand",
        "Argentina", "Chile", "Colombia", "Ireland", "Portugal",
        "Switzerland", "Belgium", "Austria", "Denmark", "Greece",
        "Turkey", "Israel", "Singapore", "Malaysia", "Philippines",
        "Thailand", "Vietnam", "South Korea", "Saudi Arabia", "UAE"
    ]

    athletes = []

    for _ in range(num_athletes):
        name = random.choice(names)
        age = random.randint(10, 70)
        time = round(random.uniform(9.56, 12.99), 2)
        country = random.choice(countries)
        athletes.append((name, age, time, country))

    # Sort athletes by time
    athletes.sort(key=lambda x: x[2])
    
    return athletes

def main():
    num_athletes = 50
    athlete_data = generate_athlete_data(num_athletes)

    print("Athlete Data (Name, Age, Time, Country):")
    for athlete in athlete_data:
        print(athlete)

if __name__ == "__main__":
    main()