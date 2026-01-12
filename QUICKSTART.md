# 🚀 Quick Start - AI Agent Skills

¡Empieza a usar los Agent Skills en 5 minutos!

## ⚡ Instalación Rápida

### Opción 1: Claude Code (Más Fácil)

```bash
# Copiar un skill a tu directorio personal
cp -r skills/code-analysis ~/.claude/skills/

# ¡Listo! Claude lo detectará automáticamente
```

**Uso:**
```
Tú: "Analiza el código en main.py"
Claude: [Usa code-analysis skill automáticamente] ✨
```

---

### Opción 2: Claude.ai (Interfaz Web)

1. **Empaqueta el skill:**
   ```bash
   ./package-skills.sh code-analysis
   ```

2. **Sube a Claude.ai:**
   - Abre [Claude.ai](https://claude.ai)
   - Ve a Settings ⚙️ > Features
   - Click en "Upload Skill"
   - Selecciona `packaged-skills/code-analysis.zip`

3. **¡Úsalo!**
   ```
   "Revisa mi código y dame feedback"
   ```

---

### Opción 3: Claude API (Programático)

```python
import anthropic

client = anthropic.Anthropic(api_key="tu-api-key")

# 1. Subir skill
with open("packaged-skills/code-analysis.zip", "rb") as f:
    skill = client.skills.create(file=f, name="code-analysis")

# 2. Usar en conversación
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
        "content": "Analiza este código y sugiere mejoras"
    }],
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "files-api-2025-04-14"
    ]
)

print(response.content[0].text)
```

---

## 🎯 Skills Disponibles

| Skill | Descripción | Úsalo Para |
|-------|-------------|------------|
| **code-analysis** | Análisis de calidad de código | Revisiones de código, detección de code smells |
| **documentation** | Generación de documentación | README, API docs, guías técnicas |
| **testing** | Creación de tests | Unit tests, integration tests, TDD |
| **architecture** | Diseño de sistemas | System design, patrones, escalabilidad |
| **refactoring** | Mejora de código | Modernización, deuda técnica, patterns |

---

## 💡 Ejemplos Rápidos

### 📊 Analizar Código

```python
# Tu código
def calc(a, b, c):
    x = a + b
    if c:
        return x * 2
    return x

# Claude con code-analysis skill:
# ✅ Detecta nombres poco claros
# ✅ Sugiere type hints
# ✅ Recomienda docstrings
# ✅ Calcula complejidad
```

### 📝 Generar Documentación

```python
# Tu función
def process_payment(amount, user_id):
    # código aquí
    pass

# Claude con documentation skill:
# ✅ Genera docstring completo
# ✅ Añade ejemplos de uso
# ✅ Documenta excepciones
# ✅ Sigue convenciones del lenguaje
```

### 🧪 Crear Tests

```python
# Tu código
def validate_email(email):
    return "@" in email and "." in email

# Claude con testing skill:
# ✅ Genera tests con pytest
# ✅ Cubre casos válidos e inválidos
# ✅ Usa fixtures apropiadas
# ✅ Incluye edge cases
```

---

## 🔧 Comandos Útiles

```bash
# Empaquetar todos los skills
./package-skills.sh

# Empaquetar skill específico
./package-skills.sh code-analysis

# Ver estructura del proyecto
cat STRUCTURE.md

# Leer guía de uso completa
cat USAGE_GUIDE.md

# Ver cómo contribuir
cat CONTRIBUTING.md
```

---

## 📚 Aprende Más

- **Guía Completa:** `USAGE_GUIDE.md`
- **Estructura:** `STRUCTURE.md`
- **Contribuir:** `CONTRIBUTING.md`
- **Ejemplos de Código:** `examples/`
- **Docs Oficiales:** [Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

---

## 🎓 Ejemplos de Prompts Efectivos

### Con code-analysis:
- ✅ "Analiza main.py y dame un reporte detallado"
- ✅ "Revisa este código y encuentra code smells"
- ✅ "Calcula la complejidad ciclomática de estas funciones"

### Con documentation:
- ✅ "Genera un README completo para este proyecto"
- ✅ "Documenta esta API REST con ejemplos"
- ✅ "Crea docstrings para todas las funciones"

### Con testing:
- ✅ "Genera tests unitarios para UserService"
- ✅ "Crea tests de integración para esta API"
- ✅ "Implementa TDD para esta nueva feature"

### Con architecture:
- ✅ "Diseña la arquitectura para un sistema de chat"
- ✅ "Evalúa estas opciones de arquitectura"
- ✅ "Crea un ADR para esta decisión técnica"

### Con refactoring:
- ✅ "Refactoriza este código legacy"
- ✅ "Moderniza este código a Python 3.12"
- ✅ "Elimina esta deuda técnica paso a paso"

---

## 🆘 Problemas Comunes

### El skill no se activa
**Solución:** Sé más explícito en tu solicitud:
- ❌ "Mira este código"
- ✅ "Analiza la calidad de este código"

### Error al empaquetar
**Solución:** Verifica permisos:
```bash
chmod +x package-skills.sh
./package-skills.sh
```

### Skill no aparece en Claude Code
**Solución:** Verifica la ubicación:
```bash
ls ~/.claude/skills/
# o
ls .claude/skills/
```

---

## 🎉 ¡Listo para Empezar!

```bash
# 1. Empaqueta el skill que necesites
./package-skills.sh code-analysis

# 2. Úsalo en tu plataforma favorita
#    - Claude Code: cp -r skills/code-analysis ~/.claude/skills/
#    - Claude.ai: Sube el ZIP desde Settings
#    - Claude API: Usa el ejemplo en examples/api_example.py

# 3. ¡Disfruta de Claude con superpoderes! 🚀
```

---

**¿Preguntas?** Lee `USAGE_GUIDE.md` o abre un issue en GitHub.

**¡Feliz coding!** 👨‍💻👩‍💻
