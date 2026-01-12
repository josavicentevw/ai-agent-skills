# Guía de Uso - AI Agent Skills

Esta guía te ayudará a comenzar a usar los Agent Skills en diferentes plataformas.

## 📋 Tabla de Contenidos

- [Inicio Rápido](#inicio-rápido)
- [Uso en Claude API](#uso-en-claude-api)
- [Uso en Claude Code](#uso-en-claude-code)
- [Uso en Claude.ai](#uso-en-claudeai)
- [Ejemplos de Uso](#ejemplos-de-uso)

## 🚀 Inicio Rápido

### Paso 1: Empaquetar Skills

Primero, empaqueta los skills que quieras usar:

```bash
# Empaquetar todos los skills
./package-skills.sh

# O empaquetar un skill específico
./package-skills.sh code-analysis
```

Esto creará archivos ZIP en el directorio `packaged-skills/`.

## 🔧 Uso en Claude API

### Prerequisitos

- API key de Anthropic
- Python 3.8+
- SDK de Anthropic instalado: `pip install anthropic`

### Configuración Básica

```python
import anthropic

client = anthropic.Anthropic(api_key="tu-api-key")

# Subir un skill
with open("packaged-skills/code-analysis.zip", "rb") as f:
    skill = client.skills.create(file=f, name="code-analysis")

print(f"Skill ID: {skill.id}")
```

### Usar el Skill en una Conversación

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=[{"type": "code_execution_2025_08_25"}],
    container={
        "type": "code_execution_container",
        "skill_ids": [skill.id]
    },
    messages=[{
        "role": "user",
        "content": "Analiza el archivo main.py y dame recomendaciones"
    }],
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "files-api-2025-04-14"
    ]
)

# Procesar respuesta
for block in response.content:
    if hasattr(block, "text"):
        print(block.text)
```

### Listar Skills Disponibles

```python
# Listar todos los skills en tu organización
skills = client.skills.list()
for skill in skills.data:
    print(f"{skill.name} (ID: {skill.id})")
```

### Eliminar un Skill

```python
client.skills.delete(skill_id="skill-id-aqui")
```

## 💻 Uso en Claude Code

### Instalación Local

1. **Copia el skill a tu directorio personal:**

```bash
mkdir -p ~/.claude/skills
cp -r skills/code-analysis ~/.claude/skills/
```

2. **O copia a un proyecto específico:**

```bash
mkdir -p .claude/skills
cp -r skills/code-analysis .claude/skills/
```

### Uso

Claude Code descubrirá automáticamente los skills disponibles. Simplemente menciona lo que necesitas:

```
Tú: "Analiza el código en src/main.py"
Claude: [Usa automáticamente el skill code-analysis]
```

### Verificar Skills Instalados

```bash
ls ~/.claude/skills/
# o
ls .claude/skills/
```

## 🌐 Uso en Claude.ai

### Subir un Skill

1. Ve a **Settings** > **Features**
2. En la sección **Skills**, haz clic en **Upload Skill**
3. Selecciona el archivo ZIP del skill (de `packaged-skills/`)
4. Espera la confirmación de carga

### Usar un Skill

Una vez cargado, Claude lo usará automáticamente cuando sea relevante:

```
Tú: "Revisa el código de este proyecto y dame feedback"
Claude: [Activará el skill code-analysis automáticamente]
```

### Gestionar Skills

- **Ver skills instalados:** Settings > Features > Skills
- **Eliminar skill:** Haz clic en el ícono de papelera junto al skill
- **Actualizar skill:** Elimina el anterior y sube la nueva versión

### Limitaciones en Claude.ai

- Los skills son **por usuario** (no compartidos con el equipo)
- Acceso a red puede estar limitado según configuración
- No hay gestión centralizada por administradores

## 📚 Ejemplos de Uso

### Ejemplo 1: Análisis de Código

```python
# Skill: code-analysis
# Solicitud: "Analiza este código y dame mejoras"

def process(data):
    result = []
    for i in range(len(data)):
        if data[i] > 0:
            result.append(data[i] * 2)
    return result

# Claude detectará:
# - Uso innecesario de range(len())
# - Oportunidad para comprensión de lista
# - Falta de type hints
# - Sugerirá versión mejorada
```

### Ejemplo 2: Generación de Documentación

```python
# Skill: documentation
# Solicitud: "Documenta esta función"

def calculate_discount(price, customer_type):
    if customer_type == "premium":
        return price * 0.8
    return price * 0.95

# Claude generará docstring completo:
# - Descripción de la función
# - Parámetros con tipos
# - Valor de retorno
# - Ejemplos de uso
```

### Ejemplo 3: Generación de Tests

```python
# Skill: testing
# Solicitud: "Genera tests para esta función"

def add_user(name, email):
    if not email:
        raise ValueError("Email required")
    return {"name": name, "email": email}

# Claude generará:
# - Tests unitarios con pytest
# - Casos felices y edge cases
# - Tests de validación
# - Fixtures si son necesarios
```

### Ejemplo 4: Diseño de Arquitectura

```
Skill: architecture
Solicitud: "Diseña la arquitectura para un sistema de e-commerce"

Claude generará:
- Diagrama de componentes
- Patrones recomendados (microservicios, event-driven, etc.)
- Stack tecnológico sugerido
- Consideraciones de escalabilidad
- Trade-offs de cada decisión
```

### Ejemplo 5: Refactoring

```python
# Skill: refactoring
# Solicitud: "Refactoriza este código"

class User:
    def __init__(self, n, e, a, c, s, z):
        self.n = n
        self.e = e
        self.a = a
        self.c = c
        self.s = s
        self.z = z

# Claude:
# 1. Mejorará nombres de variables
# 2. Extraerá Address como clase separada
# 3. Añadirá type hints
# 4. Añadirá docstrings
# 5. Implementará __repr__ y __eq__
```

## 🔄 Combinar Múltiples Skills

Puedes usar varios skills en una misma sesión:

```python
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    tools=[{"type": "code_execution_2025_08_25"}],
    container={
        "type": "code_execution_container",
        "skill_ids": [
            "code-analysis-skill-id",
            "refactoring-skill-id",
            "testing-skill-id"
        ]
    },
    messages=[{
        "role": "user",
        "content": "Analiza este código, refactorízalo y genera tests"
    }],
    # ... betas
)
```

## 📊 Monitoreo y Debug

### Ver qué Skill se Activó

En la respuesta de Claude, verás referencias a los skills usados:

```
🔧 Activando skill: code-analysis
📖 Leyendo: code-analysis/SKILL.md
✅ Análisis completo
```

### Logs en API

```python
import logging

logging.basicConfig(level=logging.DEBUG)
# Verás las llamadas a tools y skills en los logs
```

## ⚠️ Solución de Problemas

### Skill No Se Activa

1. **Verifica que la descripción sea clara:** El skill se activa por keywords
2. **Sé explícito:** Menciona la tarea claramente
3. **Revisa el contexto:** Proporciona suficiente información

### Error al Subir Skill

1. **Verifica el formato ZIP:** Estructura correcta con SKILL.md
2. **Revisa el frontmatter:** name y description válidos
3. **Tamaño del archivo:** Skills muy grandes pueden fallar

### Skill Desactualizado

1. **En API:** Elimina y sube nueva versión
2. **En Claude.ai:** Elimina y sube nueva versión
3. **En Claude Code:** Reemplaza el directorio

## 🆘 Soporte

- **Documentación Oficial:** [Anthropic Agent Skills Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- **Issues:** [GitHub Issues](https://github.com/yourusername/ai-agent-skills/issues)
- **Ejemplos:** Ver carpeta `examples/`

## 📖 Recursos Adicionales

- [Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [API Reference](https://platform.claude.com/docs/en/build-with-claude/skills-guide)

---

¿Necesitas ayuda? Abre un issue o consulta la documentación oficial.
