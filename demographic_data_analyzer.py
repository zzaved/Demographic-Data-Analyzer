import pandas as pd  # Importa a biblioteca pandas para manipulação de dados

# Função principal que calcula e exibe dados demográficos
def calculate_demographic_data(print_data=True):
    # Lê os dados do arquivo CSV utilizando Pandas e armazena em um DataFrame chamado 'df'
    df = pd.read_csv('adult.data.csv')

    # 1. Quantas pessoas de cada raça estão representadas no dataset?
    # A coluna 'race' contém as informações sobre a raça de cada pessoa
    race_count = df['race'].value_counts()

    # 2. Qual é a idade média dos homens?
    # Filtra os dados para homens (sex == 'Male') e calcula a média da coluna 'age'
    # O valor é arredondado para 1 casa decimal
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Qual a porcentagem de pessoas que possuem diploma de Bacharelado?
    # Conta o número de pessoas com 'Bachelors' na coluna 'education' e divide pelo total de registros
    # Multiplica por 100 para obter o percentual e arredonda para 1 casa decimal
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # 4. Qual a porcentagem de pessoas com educação avançada que ganham mais de 50K?
    # Educação avançada: 'Bachelors', 'Masters' ou 'Doctorate'
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]  # Pessoas com educação avançada
    
    # Pessoas sem educação avançada
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentual de pessoas com educação avançada que ganham mais de 50K
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)

    # Percentual de pessoas sem educação avançada que ganham mais de 50K
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # 5. Qual é o número mínimo de horas que uma pessoa trabalha por semana?
    # Obtém o menor valor da coluna 'hours-per-week', que representa as horas de trabalho semanais
    min_work_hours = df['hours-per-week'].min()

    # 6. Qual a porcentagem de pessoas que trabalham o mínimo de horas por semana e ganham mais de 50K?
    # Filtra os dados para pessoas que trabalham o mínimo de horas
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    # Calcula a porcentagem das pessoas que trabalham o mínimo de horas e ganham mais de 50K
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # 7. Qual país tem a maior porcentagem de pessoas que ganham mais de 50K?
    # Conta quantas pessoas de cada país estão representadas no dataset
    countries = df['native-country'].value_counts()
    # Conta quantas pessoas de cada país ganham mais de 50K
    rich_countries = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    # Calcula a porcentagem de pessoas que ganham mais de 50K por país e encontra o país com a maior porcentagem
    highest_earning_country_percentage = round((rich_countries / countries * 100).max(), 1)
    highest_earning_country = (rich_countries / countries * 100).idxmax()

    # 8. Qual é a ocupação mais popular para quem ganha mais de 50K na Índia?
    # Filtra os dados para pessoas que são da Índia e ganham mais de 50K, então encontra a ocupação mais comum
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Se 'print_data' for verdadeiro, imprime os resultados
    if print_data:
        print("Número de cada raça:\n", race_count)
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem de pessoas com diploma de Bacharelado: {percentage_bachelors}%")
        print(f"Porcentagem com educação avançada que ganham >50K: {higher_education_rich}%")
        print(f"Porcentagem sem educação avançada que ganham >50K: {lower_education_rich}%")
        print(f"Tempo mínimo de trabalho: {min_work_hours} horas/semana")
        print(f"Porcentagem de ricos entre os que trabalham o mínimo: {rich_percentage}%")
        print("País com maior porcentagem de ricos:", highest_earning_country)
        print(f"Maior porcentagem de ricos em um país: {highest_earning_country_percentage}%")
        print("Ocupação mais comum entre os ricos na Índia:", top_IN_occupation)

    # Retorna os resultados para testes e outros usos
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }