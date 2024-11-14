class Hotel:
    def __init__(self, nome, num_quartos):
        self.nome = nome
        self.num_quartos = num_quartos
        self.quartos_disponiveis = num_quartos  # Todos os quartos estão disponíveis
        self.reservas = []  # Lista de reservas feitas

    def reservar_quarto(self, nome_cliente, num_quartos_reservados):
        if num_quartos_reservados <= self.quartos_disponiveis:
            self.quartos_disponiveis -= num_quartos_reservados
            self.reservas.append({
                "nome_cliente": nome_cliente,
                "num_quartos_reservados": num_quartos_reservados
            })
            print(f"Reserva confirmada para {nome_cliente}, {num_quartos_reservados} quarto(s).")
        else:
            print("Desculpe, não temos quartos disponíveis para a quantidade solicitada.")

    def cancelar_reserva(self, nome_cliente):
        reserva_encontrada = False
        for reserva in self.reservas:
            if reserva["nome_cliente"] == nome_cliente:
                self.quartos_disponiveis += reserva["num_quartos_reservados"]
                self.reservas.remove(reserva)
                print(f"Reserva cancelada para {nome_cliente}.")
                reserva_encontrada = True
                break
        if not reserva_encontrada:
            print("Reserva não encontrada.")

    def mostrar_disponibilidade(self):
        print(f"Quartos disponíveis: {self.quartos_disponiveis}")

    def mostrar_reservas(self):
        if not self.reservas:
            print("Não há reservas feitas.")
        else:
            print("Reservas feitas:")
            for reserva in self.reservas:
                print(f"Cliente: {reserva['nome_cliente']}, Quartos reservados: {reserva['num_quartos_reservados']}")


 #Testar a classe

def menu():
    hotel = Hotel("Hotel Exemplo", 10)  # Criar o hotel com 10 quartos

    while True:
        print("\n--- Menu ---")
        print("1. Mostrar disponibilidade")
        print("2. Fazer uma reserva")
        print("3. Cancelar uma reserva")
        print("4. Mostrar reservas")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            hotel.mostrar_disponibilidade()
        elif escolha == "2":
            nome_cliente = input("Digite seu nome: ")
            num_quartos = int(input("Quantos quartos você deseja reservar? "))
            hotel.reservar_quarto(nome_cliente, num_quartos)
        elif escolha == "3":
            nome_cliente = input("Digite o nome da reserva a ser cancelada: ")
            hotel.cancelar_reserva(nome_cliente)
        elif escolha == "4":
            hotel.mostrar_reservas()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
