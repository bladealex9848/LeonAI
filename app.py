# Importación de bibliotecas necesarias
import os
import openai
import streamlit as st
import time

import streamlit as st
import openai

# Configuración de la página
st.set_page_config(
    page_title="León AI",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://bosquesdeleon.edu.co',
        'Report a bug': None,
        'About': "León AI: Tu asistente virtual para la Institución Educativa Bosques de León. Obtén información sobre la institución, los procesos académicos y más."
    }
)

# Función para verificar si el archivo secrets.toml existe
def secrets_file_exists():
    secrets_path = os.path.join('.streamlit', 'secrets.toml')
    return os.path.isfile(secrets_path)

# Intentar obtener el ID del asistente de OpenAI desde st.secrets si el archivo secrets.toml existe
if secrets_file_exists():
    try:
        ASSISTANT_ID = st.secrets['ASSISTANT_ID']
    except KeyError:
        ASSISTANT_ID = None
else:
    ASSISTANT_ID = None

# Si no está disponible, pedir al usuario que lo introduzca
if not ASSISTANT_ID:
    ASSISTANT_ID = st.sidebar.text_input('Introduce el ID del asistente de OpenAI', type='password')

# Si aún no se proporciona el ID, mostrar un error y detener la ejecución
if not ASSISTANT_ID:
    st.sidebar.error("Por favor, proporciona el ID del asistente de OpenAI.")
    st.stop()

assistant_id = ASSISTANT_ID

# Inicialización del cliente de OpenAI
client = openai

st.title("Bienvenido a León AI 🦁")

st.write("""
        [![ver código fuente](https://img.shields.io/badge/Repositorio%20GitHub-gris?logo=github)](https://github.com/bladealex9848/LeonAI)
        ![Visitantes](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fleonai.streamlit.app&label=Visitantes&labelColor=%235d5d5d&countColor=%231e7ebf&style=flat)
        """)

st.markdown("""
### 🦁 ¡Hola! Soy León AI, tu asistente virtual para la Institución Educativa Bosques de León

Estoy aquí para brindarte información sobre la institución y responder tus preguntas.

#### ¿Qué puedo hacer por ti hoy? 🤔

* Contarte sobre la filosofía, misión, visión y políticas de la institución.
* Describir los procesos de admisión, matrícula, evaluación y promoción de estudiantes.
* Explicarte las normas de convivencia, los derechos y deberes de los estudiantes, y el uso de uniformes.
* Responder preguntas sobre eventos institucionales, como la ceremonia de graduación y la primera comunión.
* Guiarte en el acceso y uso de la plataforma virtual Cisco Webex.
* Aclarar dudas sobre los costos educativos, el proceso de inscripción y otros temas administrativos.

**¡No dudes en consultarme cualquier inquietud sobre la Institución Educativa Bosques de León!**

*Recuerda: Proporciono información general basada en la documentación disponible. Para información oficial o  trámites específicos, contacta directamente con la institución.*
""")

# Inicialización de variables de estado de sesión
st.session_state.start_chat = True
if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

# Cargar la clave API de OpenAI
API_KEY = os.environ.get('OPENAI_API_KEY') or st.secrets.get('OPENAI_API_KEY')
if not API_KEY:
    API_KEY = st.sidebar.text_input('Introduce tu clave API de OpenAI', type='password')

if not API_KEY:
    st.sidebar.error("Por favor, proporciona una clave API para continuar.")
    st.stop()

openai.api_key = API_KEY

def process_message_with_citations(message):
    """Extraiga y devuelva solo el texto del mensaje del asistente."""
    if hasattr(message, 'content') and len(message.content) > 0:
        message_content = message.content[0]
        if hasattr(message_content, 'text'):
            nested_text = message_content.text
            if hasattr(nested_text, 'value'):
                return nested_text.value
    return 'No se pudo procesar el mensaje'

# Crear un hilo de chat inmediatamente después de cargar la clave API
if not st.session_state.thread_id:
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id
    st.write("ID del hilo: ", thread.id)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("¿Cómo puedo ayudarte hoy?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("usuario"):
        st.markdown(prompt)

    # Enviar mensaje del usuario
    client.beta.threads.messages.create(
        thread_id=st.session_state.thread_id,
        role="user",
        content=prompt
    )

    # Crear una ejecución para el hilo de chat
    run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=assistant_id
    )

    while run.status != 'completed':
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_id,
            run_id=run.id
        )

    # Recuperar mensajes agregados por el asistente
    messages = client.beta.threads.messages.list(
    thread_id=st.session_state.thread_id
    )

    # Procesar y mostrar mensajes del asistente
    for message in messages:
        if message.run_id == run.id and message.role == "assistant":
            full_response = process_message_with_citations(message)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            with st.chat_message("assistant"):
                st.markdown(full_response)
                
# Footer
st.sidebar.markdown('---')
st.sidebar.subheader('Creado por:')
st.sidebar.markdown('Alexander Oviedo Fadul')
st.sidebar.markdown("[GitHub](https://github.com/bladealex9848) | [Website](https://alexanderoviedofadul.dev/) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!%20)")