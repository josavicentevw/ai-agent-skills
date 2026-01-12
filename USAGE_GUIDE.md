# Guía de Uso - AI Agent Skills

Esta guía te ayudará a comenzar a usar los Agent Skills en diferentes plataformas.

## 📋 Tabla de Contenidos

- [Inicio Rápido](#inicio-rápido)
- [🤖 Uso con GitHub Copilot (VS Code) - RECOMENDADO](#-uso-con-github-copilot-vs-code---recomendado)
- [Uso en Claude API](#uso-en-claude-api)
- [Uso en Claude Code](#uso-en-claude-code)
- [Uso en Claude.ai](#uso-en-claudeai)
- [Ejemplos de Uso](#ejemplos-de-uso)

## 🚀 Inicio Rápido

### Método 1: GitHub Copilot en VS Code (RECOMENDADO)

```bash
# 1. Copia los skills a tu proyecto
mkdir -p .github/skills
cp -r skills/* .github/skills/

# 2. Habilita Agent Skills en VS Code
# Settings → chat.useAgentSkills → ✅

# 3. ¡Listo! Copilot los usará automáticamente
```

### Método 2: Claude Code o Claude API

```bash
# Empaqueta los skills que quieras usar
./package-skills.sh code-analysis

# Esto creará archivos ZIP en packaged-skills/
```

📖 **[Ver Guía de Inicio Rápido Completa →](QUICKSTART.md)**

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

---

## 🤖 Uso con GitHub Copilot (VS Code) - RECOMENDADO

**Agent Skills es un estándar abierto soportado nativamente por GitHub Copilot en VS Code.** Este es el método recomendado para usar los skills en tu flujo de trabajo diario.

### ¿Por qué usar GitHub Copilot con Agent Skills?

✅ **Integración nativa**: No requiere API keys externas
✅ **Activación automática**: Los skills se cargan cuando son relevantes
✅ **Estándar abierto**: Compatible con múltiples agentes AI (Copilot, Claude, etc.)
✅ **Portable**: Los skills funcionan en VS Code, Copilot CLI, y Copilot coding agent
✅ **Eficiente**: Progressive disclosure - solo carga lo necesario
✅ **Compartible**: Skills de proyecto (`.github/skills/`) se comparten con el equipo

### Prerequisitos

- VS Code con GitHub Copilot extension instalada
- VS Code versión 1.108 o superior
- GitHub Copilot activo en tu cuenta

### Instalación

#### Opción A: Skills de Proyecto (Recomendado)

Los skills se comparten con todo el equipo vía git:

```bash
# En la raíz de tu repositorio
mkdir -p .github/skills

# Copia los skills que necesites
cp -r skills/code-analysis .github/skills/
cp -r skills/testing .github/skills/
cp -r skills/product-owner .github/skills/

# Commit al repositorio
git add .github/skills
git commit -m "feat: Add Agent Skills for team"
git push
```

#### Opción B: Skills Personales

Skills solo para ti, disponibles en todos tus proyectos:

```bash
# Crea directorio en tu home
mkdir -p ~/.github/skills

# Copia los skills
cp -r skills/* ~/.github/skills/
```

### Configuración en VS Code

1. **Habilitar Agent Skills** (Feature Preview):
   ```
   Settings (Cmd/Ctrl + ,) → Buscar "chat.useAgentSkills" → ✅ Activar
   ```

2. **Verificar que los skills están disponibles**:
   - Abre GitHub Copilot Chat (`Ctrl+Cmd+I` / `Ctrl+Alt+I`)
   - Los skills se activarán automáticamente cuando sean relevantes

### Estructura de Directorios

```
tu-proyecto/
├── .github/
│   └── skills/              # ✅ Recomendado (compartido con equipo)
│       ├── code-analysis/
│       │   ├── SKILL.md
│       │   ├── EXAMPLES_STACK.md
│       │   └── scripts/
│       ├── testing/
│       │   ├── SKILL.md
│       │   └── EXAMPLES_STACK.md
│       ├── product-owner/
│       │   └── SKILL.md
│       └── engineering-manager/
│           └── SKILL.md
│
# O en tu home (solo para ti):
~/.github/skills/            # ✅ Personal (todos tus proyectos)
    ├── code-analysis/
    ├── testing/
    └── ...
```

**Nota**: También se soporta `.claude/skills/` para compatibilidad legacy, pero se recomienda `.github/skills/`.

### Uso Diario

Los skills se activan **automáticamente** basándose en tu prompt. No necesitas seleccionarlos manualmente.

#### Ejemplos de Uso

**1. Análisis de Código (activa skill `code-analysis`)**

```
💬 Copilot Chat:
"Analiza el componente UserProfile.tsx y dame recomendaciones de mejora"

🔧 Copilot:
- Detecta automáticamente el skill code-analysis
- Carga SKILL.md y EXAMPLES_STACK.md
- Analiza el código React/TypeScript
- Proporciona sugerencias específicas del stack
```

**2. Crear Tests (activa skill `testing`)**

```
💬 Copilot Chat:
"Genera tests completos para el servicio UserService usando Jest"

🔧 Copilot:
- Activa skill testing
- Usa ejemplos de EXAMPLES_STACK.md para Jest
- Genera unit tests, integration tests, mocks
- Incluye casos edge y manejo de errores
```

**3. User Stories (activa skill `product-owner`)**

```
💬 Copilot Chat:
"Escribe una user story para la feature de login social con OAuth"

🔧 Copilot:
- Activa skill product-owner
- Usa formato de user story del SKILL.md
- Incluye acceptance criteria
- Agrega estimaciones y prioridad
```

**4. Performance Review (activa skill `engineering-manager`)**

```
💬 Copilot Chat:
"Ayúdame a preparar una performance review para un senior engineer"

🔧 Copilot:
- Activa skill engineering-manager
- Usa template de performance review
- Estructura con goals, competencias, feedback
```

### Cómo Funciona (Progressive Disclosure)

GitHub Copilot usa un sistema de carga en 3 niveles:

**Nivel 1: Discovery**
- Copilot siempre conoce qué skills están disponibles
- Lee `name` y `description` del frontmatter YAML
- Decide qué skill es relevante para tu prompt

**Nivel 2: Instructions Loading**
- Cuando tu prompt coincide con la descripción del skill
- Copilot carga el contenido del `SKILL.md` completo
- Las instrucciones detalladas están ahora disponibles

**Nivel 3: Resource Access**
- Copilot accede a archivos adicionales solo si son necesarios
- Scripts, ejemplos, docs en el directorio del skill
- Se cargan bajo demanda para mantener el contexto eficiente

**Beneficio**: Puedes instalar muchos skills sin consumir contexto innecesariamente.

### Skills por Rol

#### Desarrolladores
```bash
cp -r skills/code-analysis .github/skills/
cp -r skills/testing .github/skills/
cp -r skills/refactoring .github/skills/
cp -r skills/documentation .github/skills/
cp -r skills/architecture .github/skills/
```

#### Product Managers
```bash
cp -r skills/product-owner .github/skills/
```

#### Engineering Managers
```bash
cp -r skills/engineering-manager .github/skills/
cp -r skills/architecture .github/skills/
```

#### HR Team
```bash
cp -r skills/human-resources .github/skills/
```

#### Marketing Team
```bash
cp -r skills/marketing .github/skills/
cp -r skills/communications .github/skills/
```

### Verificar Skills Instalados

```bash
# Ver skills de proyecto
ls -1 .github/skills/

# Ver skills personales
ls -1 ~/.github/skills/
```

### Ventajas vs Claude API/Code

| Característica | GitHub Copilot + Skills | Claude API/Code |
|----------------|------------------------|------------------|
| **Instalación** | Copy & paste | Requiere empaquetado ZIP |
| **Activación** | Automática por prompt | Manual o programática |
| **API Key** | No requerida (con Copilot) | Sí (Anthropic API key) |
| **Compartir con equipo** | ✅ Vía git (.github/skills/) | ❌ Individual |
| **Portable** | ✅ VS Code, CLI, coding agent | ✅ Claude platforms |
| **Costo** | Incluido en Copilot | Consumo de tokens API |
| **Integración IDE** | ✅ Nativa en VS Code | Requiere extensión |

### Troubleshooting

**❓ Los skills no se activan**

1. Verifica que `chat.useAgentSkills` está habilitado
2. Asegúrate de que los skills están en `.github/skills/` o `~/.github/skills/`
3. Revisa que cada skill tiene un `SKILL.md` válido con frontmatter YAML
4. Reinicia VS Code si acabas de agregar skills

**❓ Copilot no encuentra el skill correcto**

- Mejora la descripción en el frontmatter YAML del `SKILL.md`
- Sé más específico en tu prompt (menciona keywords de la descripción)

**❓ Quiero ver qué skill se activó**

- Observa el contexto de la respuesta de Copilot
- Los skills cargados deberían influenciar el formato de la respuesta

### Recursos Oficiales

- **VS Code Docs**: https://code.visualstudio.com/docs/copilot/customization/agent-skills
- **Agent Skills Spec**: https://agentskills.io/
- **GitHub Awesome Copilot**: https://github.com/github/awesome-copilot
- **Anthropic Skills**: https://github.com/anthropics/skills

---

## 🔀 Flujo de Trabajo Híbrido: Copilot + Claude

Los Agent Skills también pueden complementar tu flujo de trabajo con GitHub Copilot. Aunque Copilot y Claude son herramientas diferentes, puedes integrar conceptualmente los skills en tu proceso de desarrollo diario.

### Enfoque Híbrido: Copilot + Agent Skills

#### 1. **Copilot para Autocompletado Rápido**

Usa GitHub Copilot para:
- Autocompletado de código línea por línea
- Generación rápida de funciones pequeñas
- Snippets y boilerplate code
- Refactorizaciones simples

```typescript
// Copilot te ayuda con autocompletado inline
function calculateDiscount(price: number, customer: Customer) {
  // Escribe el comentario y Copilot sugiere la implementación
  // Calculate discount based on customer tier
  
}
```

#### 2. **Claude + Skills para Análisis Profundo**

Usa Claude con Agent Skills para:
- **Análisis completo de arquitectura**
- **Revisión exhaustiva de código**
- **Generación de tests comprehensivos**
- **Documentación detallada**
- **Refactorings complejos**

```bash
# Ejemplo: Exporta tu código para análisis con Claude
git diff > changes.patch

# Luego pega en Claude con prompt:
# "Usando el skill code-analysis, revisa estos cambios y dame feedback detallado"
```

### Flujo de Trabajo Recomendado

#### Desarrollo Diario con Copilot

1. **Escribe código con Copilot activo**
   ```typescript
   // Copilot te asiste con sugerencias inline
   export class UserService {
     constructor(private repo: UserRepository) {}
     
     async createUser(data: CreateUserDTO) {
       // Copilot sugiere validaciones y lógica
     }
   }
   ```

2. **Usa Copilot Chat para preguntas rápidas**
   - "How do I handle errors in async functions?"
   - "Generate a unit test for this function"
   - "Explain this regex pattern"

3. **Commit frecuentemente**
   ```bash
   git add .
   git commit -m "feat: add user service"
   ```

#### Revisión Profunda con Claude Skills

4. **Análisis de Código Periódico**
   
   Una vez por día/semana, usa Claude con el skill `code-analysis`:
   
   ```
   Prompt: "Revisa los archivos en src/services/ y dame:
   1. Problemas de arquitectura
   2. Violaciones de SOLID
   3. Code smells
   4. Sugerencias de mejora"
   ```

5. **Generación de Tests Completos**
   
   Usa el skill `testing` para cobertura comprehensiva:
   
   ```
   Prompt: "Genera tests completos para UserService incluyendo:
   - Unit tests con mocks
   - Integration tests
   - Edge cases
   - Error handling"
   ```

6. **Documentación de Features**
   
   Al finalizar una feature, usa el skill `documentation`:
   
   ```
   Prompt: "Documenta el módulo de autenticación:
   - README técnico
   - API documentation
   - Architecture decision records
   - Deployment guide"
   ```

### Integración en CI/CD

#### Pre-commit Hook con Claude

Crea un script que valide código antes de commit:

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Obtener archivos modificados
FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(ts|js|py|java|kt)$')

if [ -z "$FILES" ]; then
  exit 0
fi

# Crear un archivo temporal con los cambios
git diff --cached > /tmp/changes.patch

# Opcional: Llamar a Claude API con skill code-analysis
# (requiere configuración de API key)
echo "💡 Considera revisar estos cambios con Claude skill 'code-analysis'"
echo "Archivos modificados:"
echo "$FILES"

exit 0
```

#### GitHub Actions con Claude

```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Get changed files
        id: files
        run: |
          git diff origin/main...HEAD > changes.patch
      
      - name: AI Review Comment
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '🤖 **Tip**: Review this PR with Claude using the `code-analysis` skill for deeper insights!'
            })
```

### Comandos Útiles del Ecosistema

#### VS Code con Copilot

```
# Comandos en Command Palette (Cmd+Shift+P / Ctrl+Shift+P)
> GitHub Copilot: Explain This
> GitHub Copilot: Generate Tests
> GitHub Copilot: Fix This
```

#### Claude Desktop con Skills

Si usas Claude Desktop App:

1. **Arrastra carpetas de código** directamente a la ventana
2. **Menciona el skill explícitamente**:
   ```
   "Usando @code-analysis, revisa este proyecto"
   ```
3. **Exporta resultados** como Markdown para documentación

### Best Practices: Copilot + Claude

| Herramienta | Cuándo Usar | Ejemplo |
|-------------|-------------|---------|
| **GitHub Copilot** | Escritura activa de código, autocompletado, refactors simples | Escribir funciones, generar tests básicos, explicar líneas |
| **Claude + Skills** | Análisis arquitectónico, revisiones profundas, documentación compleja | Code reviews, análisis de patterns, diseño de arquitectura |

#### ✅ DO: Usar Copilot

- Autocompletar implementaciones obvias
- Generar boilerplate (modelos, DTOs, interfaces)
- Escribir tests unitarios simples
- Explicar fragmentos de código puntuales
- Sugerencias inline mientras escribes

#### ✅ DO: Usar Claude + Skills

- Revisar PRs complejos o grandes refactors
- Analizar arquitectura de múltiples archivos
- Generar suites de tests completas (unit + integration)
- Escribir documentación técnica extensa
- Diseñar nuevos features o sistemas
- Identificar code smells y anti-patterns

### Extensiones Recomendadas

Para maximizar tu productividad:

**VS Code Extensions:**
- `GitHub.copilot` - Copilot oficial
- `GitHub.copilot-chat` - Chat con Copilot
- `GitHub.copilot-labs` - Features experimentales
- `Anthropic.claude-dev` - (Si disponible) Integración Claude

**Claude Desktop:**
- Instala skills localmente en `~/.claude/skills/`
- Usa proyectos de Claude para mantener contexto entre sesiones

### Ejemplo Real: Feature Completa

```
📝 FASE 1: Diseño (Claude + architecture skill)
→ "Diseña la arquitectura para un sistema de notificaciones real-time"
→ Obtienes: diagrama, tech stack, patterns

💻 FASE 2: Implementación (GitHub Copilot)
→ Escribes código con autocompletado de Copilot
→ Generas tests básicos con Copilot

🔍 FASE 3: Revisión (Claude + code-analysis skill)
→ "Revisa el código de src/notifications/"
→ Obtienes: feedback detallado, mejoras

🧪 FASE 4: Testing (Claude + testing skill)
→ "Genera tests completos para NotificationService"
→ Obtienes: unit, integration, edge cases

📚 FASE 5: Documentación (Claude + documentation skill)
→ "Documenta el módulo de notificaciones"
→ Obtienes: README, API docs, ADRs
```

### Troubleshooting: Copilot + Claude

**Problema:** Copilot sugiere código que Claude critica

**Solución:**
1. Usa Copilot para velocidad inicial
2. Revisa con Claude antes de hacer PR
3. Ajusta sugerencias de Copilot basándote en feedback de Claude

**Problema:** Claude da feedback muy detallado, Copilot es muy rápido

**Solución:**
- **Desarrollo iterativo:** Copilot para prototipar
- **Revisión periódica:** Claude para validar calidad
- **Balance:** 80% Copilot (coding) + 20% Claude (review)

### Recursos

- **GitHub Copilot Docs:** https://docs.github.com/copilot
- **Claude Skills Docs:** https://platform.claude.com/docs/en/agents-and-tools/agent-skills
- **VS Code Copilot:** https://marketplace.visualstudio.com/items?itemName=GitHub.copilot

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
