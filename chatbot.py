from datetime import datetime

class Mensagem:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.data_envio = datetime.now()
    
    def enviar(self, canal, destino):
        print(f"[{self.data_envio}] Enviando mensagem para {destino} via {canal}: {self.conteudo}")

class MensagemVideo(Mensagem):
    def __init__(self, conteudo, arquivo, formato, duracao):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato
        self.duracao = duracao

    def enviar(self, canal, destino):
        print(f"[{self.data_envio}] Enviando vídeo '{self.arquivo}' ({self.formato}, {self.duracao}s) para {destino} via {canal}: {self.conteudo}")

class MensagemFoto(Mensagem):
    def __init__(self, conteudo, arquivo, formato):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato

    def enviar(self, canal, destino):
        print(f"[{self.data_envio}] Enviando foto '{self.arquivo}' ({self.formato}) para {destino} via {canal}: {self.conteudo}")

class MensagemArquivo(Mensagem):
    def __init__(self, conteudo, arquivo, formato):
        super().__init__(conteudo)
        self.arquivo = arquivo
        self.formato = formato

    def enviar(self, canal, destino):
        print(f"[{self.data_envio}] Enviando arquivo '{self.arquivo}' ({self.formato}) para {destino} via {canal}: {self.conteudo}")

class Canal:
    def __init__(self, nome):
        self.nome = nome

    def enviar_mensagem(self, mensagem, destino):
        mensagem.enviar(self.nome, destino)

whatsapp = Canal("WhatsApp")
telegram = Canal("Telegram")
facebook = Canal("Facebook")
instagram = Canal("Instagram")

mensagem_texto = Mensagem("Olá, como está?")
mensagem_video = MensagemVideo("Confira este vídeo!", "video.mp4", "MP4", 30)
mensagem_foto = MensagemFoto("Veja esta imagem!", "imagem.jpg", "JPEG")
mensagem_arquivo = MensagemArquivo("Aqui está seu documento", "relatorio.pdf", "PDF")

whatsapp.enviar_mensagem(mensagem_texto, "+55 11 98765-4321")
telegram.enviar_mensagem(mensagem_video, "@usuario_telegram")
facebook.enviar_mensagem(mensagem_foto, "usuario_facebook")
instagram.enviar_mensagem(mensagem_arquivo, "usuario_instagram")
