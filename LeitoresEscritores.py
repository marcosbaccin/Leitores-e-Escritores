import threading
import time


class ReaderWriter:
    def __init__(self):
        self.rd = threading.Semaphore()  # inicializa os semáforos usando a classe Semaphore no módulo de threading para leitura e escrita
        self.wrt = threading.Semaphore()
        self.readCount = 0  # inicializando o número de leitor presente

    def reader(self):
        while True:
            self.rd.acquire()  # espere ler o semáforo
            self.readCount += 1  # aumentar a contagem do leitor em 1
            if self.readCount == 1:  # uma vez que o leitor está presente, evite escrever nos dados
                self.wrt.acquire()  # espere escrever no semáforo
            self.rd.release()  # sinal na leitura do semáforo
            print(f"Reader {self.readCount} is reading")
            self.rd.acquire()  # espere ler o semáforo
            self.readCount -= 1  # leitura realizada pelo leitor, portanto, diminuindo a contagem de leitores
            if self.readCount == 0:  # se nenhum leitor estiver presente, permitir que o escritor escreva os dados
                self.wrt.release()  # sinal no semáforo de gravação, agora o escritor pode escrever
            self.rd.release()  # sinal na leitura do semáforo
            time.sleep(3)

    def writer(self):
        while True:
            self.wrt.acquire()  # espere escrever no semáforo
            print("Wrting data.....")  # escreva os dados
            print("-" * 20)
            self.wrt.release()  # sinal no semáforo de gravação
            time.sleep(3)

    def main(self):
        # chamando vários leitores e escritores
        t1 = threading.Thread(target=self.reader)
        t1.start()
        t2 = threading.Thread(target=self.writer)
        t2.start()
        t3 = threading.Thread(target=self.reader)
        t3.start()
        t4 = threading.Thread(target=self.reader)
        t4.start()
        t6 = threading.Thread(target=self.writer)
        t6.start()
        t5 = threading.Thread(target=self.reader)
        t5.start()


if __name__ == "__main__":
    c = ReaderWriter()
    c.main()
