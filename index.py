from datetime import datetime, timedelta
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')
    

@app.route('/procesar', methods=['POST'])
def procesar():
    A = request.form['InputA']
    B = request.form['InputB']
    competencia = request.form['InputCompetencia']
    X = request.form['InputX']
    estadio = request.form['InputEstadio']
    hora = request.form['InputHora']
    c = request.form['InputC']
    canal = request.form['InputCanal']
    app = request.form['InputApp']
    dia = request.form['InputFecha']
    arbitro_central = request.form['InputAr1']
    arbitro_asistente1 = request.form['InputAr2']
    arbitro_asistente2 = request.form['InputAr3']
    cuarto_arbitro = request.form['InputAr4']
    arbitro_VAR = request.form['InputAr5']
    arbitro_AVAR = request.form['InputAr6']
    paisestadio = request.form['InputAr7']
    def funcion(A, B, competencia, X, estadio, hora, c, canal, app, dia, arbitro_central, arbitro_asistente1, arbitro_asistente2, cuarto_arbitro, arbitro_VAR, arbitro_AVAR, paisestadio):
        hora = datetime.strptime(hora, "%I:%M %p")
        texto_final = f'''
        {A} vs {B} EN VIVO minuto a minuto en {competencia}
        Cobertura del partido {A} vs {B} en vivo y en tiempo real, correspondiente a la jornada {X} de la {competencia}. Horario del partido {A} vs {B}: {hora.strftime("%I:%M")} horas (CDMX). Sigue el resultado y cómo y dónde ver la transmisión minuto a minuto en VAVEL.
        Foto
        {A} vs {B} LIVE Score Updates in {competencia} Match
        Get real-time updates on {A} vs {B} live coverage minute by minute of the match, score and result online, stream information, how to watch, TV channel, lineups, latest updates and time of the (competition and matchday) with VAVEL. Match will start at {hora} PM ET on {dia}.
        Photo
        ¡Buenas tardes a todos los lectores de VAVEL!
        Bienvenidos a la retransmisión del partido {A} vs {B} en vivo, correspondiente a la jornada {X} de la {competencia}. El encuentro tendrá lugar en el {estadio}, en punto de las {hora} horas.
        Welcome to VAVEL.com’s coverage of the {competencia} match: {A} vs {B} Live Updates!
        My name is Gibelly Agudelo and I’ll be your host for this game. We will provide you with pre-game analysis, score updates, and news as it happens live here on VAVEL (Phrase)
        El partido se jugará en el {estadio}
        El partido {A} vs {B} se jugará en el estadio {estadio} de {paisestadio} con capacidad para {c} personas.
        Foto
        The match will be played at the {estadio}
        Photo
        Título sobre el análisis de {A}
        Title on the analysis of {A}
        Título sobre el análisis de {B}
        Title on the analysis of {B}
        Equipo arbitral 
        Central {arbitro_central}
        Asistente#1: {arbitro_asistente1}
        Asistente#2: {arbitro_asistente2}
        Cuarto árbitro: {cuarto_arbitro}
        VAR: {arbitro_VAR}
        AVAR: {arbitro_AVAR}
        Who will be the referee and his assistants?
        Última alineación de {A}
        {A}'s last lineup
        Última alineación de {B}
        {B}'s last lineup
        (Nombre), (Posición) (Frase)
        (Name), (Position) (Phrase)
        (Nombre), (Posición) (Frase)
        (Name), (Position) (Phrase)
        ¿Dónde y cómo ver el {A} vs {B} en vivo? Estas son las opciones de Transmisión TV y online
        El partido será transmitido por televisión en el canal {canal}
        El {A} vs {B} puede ser sintonizado desde los streams en vivo de {app}.
        Si quieres seguir el resultado del partido en vivo por internet, VAVEL es tu mejor opción.
        Este es el horario de inicio del partido en varios países:
        Argentina: {(hora+ timedelta(hours=3)).strftime("%I:%M %p")} en (Canal) 
        Bolivia: {(hora+ timedelta(hours=2)).strftime("%I:%M %p")} en (Canal) 
        Brasil: {(hora+ timedelta(hours=3)).strftime("%I:%M %p")} en (Canal) 
        Chile: {(hora+ timedelta(hours=3)).strftime("%I:%M %p")} en (Canal) 
        Colombia: {(hora+ timedelta(hours=1)).strftime("%I:%M %p")} en (Canal) 
        Ecuador: {(hora+ timedelta(hours=1)).strftime("%I:%M %p")} en (Canal) 
        Estados Unidos (ET): {(hora+ timedelta(hours=2)).strftime("%I:%M %p")} en (Canal) 
        España: {(hora+ timedelta(hours=8)).strftime("%I:%M %p")} en (Canal) 
        México: {hora.strftime("%I:%M %p")} en (Canal) 
        Paraguay: {(hora+ timedelta(hours=2)).strftime("%I:%M %p")} en (Canal) 
        Perú: {(hora+ timedelta(hours=1)).strftime("%I:%M %p")} en (Canal) 
        Uruguay: {(hora+ timedelta(hours=3)).strftime("%I:%M %p")} en (Canal) 
        Venezuela: {(hora+ timedelta(hours=2)).strftime("%I:%M %p")} en (Canal) 
        Date, time, TV Channel and Live Streaming for {A} vs {B} match for {competencia}?
        This is the start time of the game {A} vs {B} of {dia} in several countries:
        Tabla
        How to watch {A} vs {B} Live Stream in USA?
        USA Date: {dia}
        USA Time: {(hora+ timedelta(hours=2)).strftime("%I:%M %p")} ET
        USA TV channel (English): Channel 
        USA TV channel (Spanish): Channel
        USA Internet Live Updates Commentary: VAVEL
        Sigue con VAVEL el {A} vs {B} en vivo
        En unos momentos les compartiremos las últimas novedades en nuestra cobertura del {A} vs {B} en vivo, además de la más reciente información que surja desde el {estadio}. No pierdas detalle del partido en directo y online con VAVEL.
        Follow {A} vs {B} Live Score with VAVEL
        Say something more you want to say and end with Do not miss a detail of the match {A} vs {B} live updates and commentaries of VAVEL.
        ------------------------------
        1 hora:
        Historial {A} vs {B}
        History {A} vs {B} 
        Último encuentro
        Last match
        Últimos cinco partidos – {A}
        Last five games – {A}
        Últimos cinco partidos – {B}
        Last five games – {B}
        Algo de Twitter o declaraciones o un dato curioso o estadísticas (Declaraciones, de visitante o de local, jugadores internacionales, últimos 5 partidos allá o jugadores sudamericanos)
        30 min: {A} vs {B} EN VIVO (0-0) RESET
        30 min: {A} vs {B} LIVE Score Updates (0-0) RESET
        Promedio de edad de {A}
        Alineación – {A}
        Line-up – {A} 
        Suplentes – {A}
        Substitutes – {A} 
        Promedio de edad de {B}
        Alineación – {B}
        Line-up – {B}
        Suplentes – {B}
        Substitutes – {B}
        **
        Medio tiempo: Análisis de la primera mitad
        Analysis of the first half
        **
        Final: Goles y resumen del {A} 0-0 {B} en {competencia} 2024
        Summary: {A} 0-0 {B} in {competencia} 2024
        Resumen del partido con tweet del ganador o del local en caso de empate
        Cambiar la entradilla
        Añadir video resumen de youtube
        Cambiar la foto si es necesario
        '''
        return texto_final
    xd = funcion(A, B, competencia, X, estadio, hora, c, canal, app, dia, arbitro_central, arbitro_asistente1, arbitro_asistente2, cuarto_arbitro, arbitro_VAR, arbitro_AVAR, paisestadio)
    text = f'''
        <div style="word-wrap: break-word; white-space: pre-line;">
            <p>{xd}</p>
        </div>
        '''

    return text
    
if __name__ == '__main__':
    app.run(debug=True)