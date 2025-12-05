from faker import Faker


fake = Faker()

def get_login_faker(num_casos=5):


    casos = []
    usuarios_validos = "standard_user"
    password_valido = "secret_sauce"

    for _ in range(num_casos):
        username = fake.user_name()
        password = fake.password()
        login_example = fake.boolean(chance_of_getting_true=70)  # 70% de probabilidad de ser True
       
        if fake.boolean(chance_of_getting_true=30):
            username = fake.random.choice(usuarios_validos)
            password = password_valido
            login_example = True
        else:
            username = fake.user_name() #aleatorio
            password = fake.password(length=12)
            login_example = False
       
        
        casos.append((username, password, login_example))

    return casos