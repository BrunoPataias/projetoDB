import sqlite3


# Função para conectar ao banco de dados (ou criar se não existir)
def connect_db():
    conn = sqlite3.connect('hotel_reservas.db')  # Cria ou abre o arquivo do banco de dados
    return conn


# Função para criar a tabela de reservas
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente TEXT NOT NULL,
        data_checkin TEXT NOT NULL,
        data_checkout TEXT NOT NULL,
        numero_quarto INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


# Função para fazer uma reserva
def fazer_reserva(nome_cliente, data_checkin, data_checkout, numero_quarto):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO reservas (nome_cliente, data_checkin, data_checkout, numero_quarto)
    VALUES (?, ?, ?, ?)
    ''', (nome_cliente, data_checkin, data_checkout, numero_quarto))
    conn.commit()
    conn.close()


# Função para exibir todas as reservas
def exibir_reservas():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservas')
    reservas = cursor.fetchall()
    conn.close()
    return reservas


# Função principal para interação com o usuário
def main():
    create_table()  # Cria a tabela se não existir

    while True:
        print("\nMenu de Reserva de Hotel:")
        print("1. Fazer uma nova reserva")
        print("2. Exibir todas as reservas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_cliente = input("Digite o nome do cliente: ")
            data_checkin = input("Digite a data de check-in (YYYY-MM-DD): ")
            data_checkout = input("Digite a data de check-out (YYYY-MM-DD): ")
            numero_quarto = int(input("Digite o número do quarto: "))

            fazer_reserva(nome_cliente, data_checkin, data_checkout, numero_quarto)
            print("Reserva realizada com sucesso!")

        elif opcao == '2':
            reservas = exibir_reservas()
            print("\nReservas realizadas:")
            for reserva in reservas:
                print(
                    f"ID: {reserva[0]}, Nome: {reserva[1]}, Check-in: {reserva[2]}, Check-out: {reserva[3]}, Quarto: {reserva[4]}")

        elif opcao == '3':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
