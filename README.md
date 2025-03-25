## 🏗️ Proyecto: **Amparo - Asistente Virtual Multiagente para RRHH**

`Amparo` es un sistema inteligente de asistencia virtual desarrollado para apoyar al departamento de Recursos Humanos de la empresa **Constructora del Mar II**. Este sistema utiliza una arquitectura **multiagente** basada en **LangGraph**, con agentes especializados y capacidades de recuperación de información desde la web y documentos internos.

---

### 📦 Tecnologías utilizadas

- 🧠 [LangGraph](https://www.langchain.com/langgraph) — flujo de nodos multiagente
- 🤖 [LangChain](https://www.langchain.com) — agentes ReAct, herramientas, vectores
- 🧾 [OpenAI](https://platform.openai.com) — modelo `gpt-4` para razonamiento y recuperación
- 🌐 Tavily Search — búsqueda web integrada
- 📄 FAISS + OpenAIEmbeddings — recuperación desde documentos
- 🐍 Python 3.10+
- 🔐 dotenv — manejo de variables de entorno (`OPENAI_API_KEY`)

---

### 🚀 ¿Qué puede hacer Amparo?

| Función                                | Descripción                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| 👋 **Interacción Natural**             | Detecta si una pregunta es conversacional ("¿Quién eres?") y responde como asistente. |
| 🔎 **Agente de búsqueda web**          | Usa Tavily + LLM para responder con información externa.                    |
| 📄 **Agente retriever (RAG)**          | Recupera información desde un documento interno llamado "Carga de Datos".  |
| 🧠 **Supervisor inteligente**          | Clasifica cada mensaje y decide qué agente debe actuar.                    |
| ✅ **Finalización dinámica**           | Detecta cuándo una conversación está completa y cierra el flujo.           |

---

### 🧩 Estructura del sistema

```plaintext
graph/
│
├── start → supervisor_node
│              ├── info_agent ("amparo")
│              ├── retriever_agent
│              ├── research_agent
│              └── __end__
```

- `supervisor_node`: Clasifica la intención del usuario (info vs task).
- `amparo_node`: Responde preguntas básicas sobre la asistente.
- `retriever_node`: Recupera datos desde el documento UnyRem (RAG).
- `search_node`: Consulta información desde la web (Tavily).
- Todos los nodos retornan al `supervisor` para evaluar la próxima acción.

---

### 🛠️ Configuración del entorno

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/amparo-assistant.git
cd amparo-assistant
```

2. Crea un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` con tu clave de OpenAI:

```
OPENAI_API_KEY=tu_clave_de_openai
```

---

### 📂 Archivos clave

| Archivo                          | Propósito                                            |
|----------------------------------|------------------------------------------------------|
| `main.py`                        | Punto de entrada. Inicializa el grafo.              |
| `nodes/supervisor.py`           | Nodo que enruta a los agentes.                      |
| `nodes/retriever.py`            | Nodo con embeddings + RAG (documento local).        |
| `nodes/search.py`               | Nodo con búsqueda web (Tavily).                     |
| `nodes/amparo.py`               | Nodo de respuesta para preguntas generales.         |
| `utils/intents.py`              | Función `classify_intent()` para decidir la intención del usuario. |
| `data/manual_unyrem.pdf`        | Documento utilizado por el retriever (si aplica).   |

---

### 📌 Cómo ejecutar el flujo

```python
from graph import graph

salida = graph.invoke({
    "messages": [{"role": "user", "content": "¿Cómo cargo un trabajador en UnyRem?"}],
    "graph": "amparo_graph",
    "next": ""
})
```

---

### ✅ Ejemplos de uso

```text
Usuario: ¿Cómo te llamas?
→ Agente "amparo" responde: "Soy Amparo, tu asistente de RRHH."

Usuario: ¿Cómo cargo trabajadores en el ERP?
→ Agente "retriever" busca en el documento de UnyRem.

Usuario: ¿Cuándo es el próximo feriado?
→ Agente "researcher" busca en internet.
```

---

### ✨ Ideas futuras

- Agente para impresión de documentos vía BUK.
- Agente para beneficios sindicales.
- Nodo de evaluación de satisfacción del usuario.
- Historial de conversación por sesión.

---

### 🧑‍💻 Autor

**Constructora del Mar II**  
Desarrollado por el equipo de automatización de RRHH.

---

¿Querés que lo adapte también a español completo o lo divida por secciones para usarlo como base en Notion, GitHub o documentación interna?