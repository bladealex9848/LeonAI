# Guillo 🦁

![Logo de LeonAI](https://github.com/bladealex9848/LeonAI/blob/main/assets/logo.jpg)

[![Version](https://img.shields.io/badge/versión-1.0.0-darkgreen.svg)](https://github.com/bladealex9848/LeonAI)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0-ff4b4b.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI_API-v2-00C244.svg)](https://platform.openai.com/)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-yellow.svg)](LICENSE)
[![Visitantes](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fleonai.streamlit.app&label=Visitantes&labelColor=%235d5d5d&countColor=%231e7ebf&style=flat)](https://leonai.streamlit.app)

## 🦁 Descripción

Guillo es un asistente virtual desarrollado con Streamlit y la API de OpenAI, especializado en brindar información sobre la Institución Educativa Bosques de León. Este asistente está diseñado para ayudar a estudiantes, padres, profesores y personal administrativo a obtener respuestas precisas sobre la filosofía institucional, procesos académicos, normas de convivencia y eventos escolares.

El asistente tiene acceso a documentación oficial de la institución, permitiéndole proporcionar información actualizada y confiable sobre todos los aspectos relacionados con la Institución Educativa Bosques de León, facilitando así la comunicación y el acceso a la información para toda la comunidad educativa.

## 🔍 Funcionalidades Principales

### 1. Información Institucional
- **Filosofía Institucional**: Detalles sobre la misión, visión y valores del colegio
- **Proyecto Educativo**: Información sobre el enfoque pedagógico y formativo
- **Historia y Trayectoria**: Datos sobre los orígenes y desarrollo de la institución
- **Políticas Institucionales**: Explicación de las directrices y políticas educativas

### 2. Procesos Académicos
- **Admisión y Matrícula**: Requisitos y procedimientos para nuevos estudiantes
- **Evaluación y Promoción**: Sistema de calificación y criterios de promoción
- **Calendario Académico**: Fechas importantes del año escolar
- **Niveles Educativos**: Información sobre preescolar, primaria y bachillerato

### 3. Convivencia Escolar
- **Manual de Convivencia**: Explicación de las normas y reglamentos
- **Derechos y Deberes**: Información sobre responsabilidades y derechos de los estudiantes
- **Uniformes**: Especificaciones sobre el uniforme escolar y su uso
- **Conducto Regular**: Procedimientos para resolución de conflictos

### 4. Eventos y Actividades
- **Ceremonias Institucionales**: Información sobre graduaciones y primeras comuniones
- **Actividades Extracurriculares**: Detalles sobre clubes, deportes y actividades adicionales
- **Salidas Pedagógicas**: Procesos y requisitos para excursiones escolares
- **Eventos Especiales**: Fechas y detalles de celebraciones institucionales

### 5. Recursos Tecnológicos
- **Plataforma Cisco Webex**: Guía para acceso y uso de la plataforma virtual
- **Recursos Digitales**: Información sobre herramientas educativas disponibles
- **Comunicación Digital**: Canales oficiales y protocolos de comunicación
- **Soporte Técnico**: Ayuda básica para problemas comunes con plataformas institucionales

## 🚀 Instalación

### Requisitos Previos
- Python 3.8 o superior
- Pip (administrador de paquetes de Python)
- Cuenta en OpenAI con acceso a la API
- Asistente Guillo configurado en OpenAI

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/bladealex9848/LeonAI.git
   cd LeonAI
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar credenciales**

   **Opción A: Usando variables de entorno**
   ```bash
   # En Windows
   set OPENAI_API_KEY=tu-api-key-aqui
   set ASSISTANT_ID=tu-assistant-id-aqui
   
   # En macOS/Linux
   export OPENAI_API_KEY=tu-api-key-aqui
   export ASSISTANT_ID=tu-assistant-id-aqui
   ```

   **Opción B: Usando archivo secrets.toml**
   
   Crea un archivo `.streamlit/secrets.toml` con el siguiente contenido:
   ```toml
   OPENAI_API_KEY = "tu-api-key-aqui"
   ASSISTANT_ID = "tu-assistant-id-aqui"
   ```

## ⚙️ Uso

### Iniciar la Aplicación

```bash
streamlit run app.py
```

Esto lanzará la aplicación y abrirá automáticamente una ventana del navegador en `http://localhost:8501`.

### Funcionalidades del Asistente

1. **Consultas sobre la Institución**
   - Pregunta sobre la filosofía, misión y visión institucional
   - Ejemplo: "¿Cuál es la misión de la Institución Educativa Bosques de León?"

2. **Información sobre Procesos Académicos**
   - Consulta sobre admisiones, evaluaciones, promociones
   - Ejemplo: "¿Cómo es el proceso de admisión para primaria?"

3. **Consultas sobre Convivencia**
   - Obtén información sobre normas, derechos y deberes
   - Ejemplo: "¿Cuáles son las normas sobre el uso del uniforme escolar?"

4. **Eventos Institucionales**
   - Pregunta sobre celebraciones, ceremonias y actividades
   - Ejemplo: "¿Cuándo se realiza la ceremonia de graduación?"

5. **Ayuda con Plataformas**
   - Obtén guía sobre el uso de Cisco Webex
   - Ejemplo: "¿Cómo puedo acceder a la plataforma virtual para clases?"

## ⚠️ Limitaciones

- Guillo proporciona información general basada en la documentación disponible de la institución
- Para trámites oficiales o información específica, se recomienda contactar directamente a la institución
- El asistente no realiza procesos de inscripción, matrícula o pagos
- La información proporcionada puede no estar completamente actualizada si ha habido cambios recientes

## 📊 Escenarios de Uso

### 1. Estudiantes
- Consulta de normas y procedimientos académicos
- Información sobre actividades extracurriculares
- Aclaración de dudas sobre derechos y deberes

### 2. Padres de Familia
- Orientación sobre procesos de admisión y matrícula
- Información sobre costos educativos y requisitos
- Consultas sobre el calendario escolar y eventos

### 3. Personal Docente y Administrativo
- Acceso rápido a información institucional
- Referencia sobre procesos y procedimientos
- Apoyo para atención a consultas frecuentes

## 👥 Contribuciones

Las contribuciones son bienvenidas. Para contribuir al desarrollo de Guillo:

1. Realiza un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Implementa tus cambios
4. Envía un pull request

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- **OpenAI** por proporcionar la tecnología que impulsa el asistente
- **Streamlit** por facilitar el desarrollo de interfaces intuitivas
- **Institución Educativa Bosques de León** por la información y documentación proporcionada

## 👤 Autor

Creado con ❤️ por [Alexander Oviedo Fadul](https://github.com/bladealex9848)

[GitHub](https://github.com/bladealex9848) | [Website](https://alexanderoviedofadul.dev/) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!%20)

---

## 💼 Mensaje Final

Guillo busca facilitar el acceso a la información sobre la Institución Educativa Bosques de León, promoviendo una comunicación más eficiente entre la institución y su comunidad educativa. Este asistente es una herramienta de apoyo que complementa los canales oficiales de comunicación de la institución.

*"La educación es el arma más poderosa que puedes usar para cambiar el mundo. En la Institución Educativa Bosques de León trabajamos cada día para formar ciudadanos íntegros, competentes y comprometidos con su entorno."*