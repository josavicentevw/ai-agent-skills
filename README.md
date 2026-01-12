# AI Agent Skills Collection

Una colección de Agent Skills profesionales siguiendo las mejores prácticas de Anthropic para extender las capacidades de Claude con expertise especializado.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-10-blue.svg)]()
[![Documentation](https://img.shields.io/badge/Docs-Completo-green.svg)]()

## 🚀 Quick Start

```bash
# 1. Empaqueta un skill
./package-skills.sh code-analysis

# 2. Usa con Claude Code
cp -r skills/code-analysis ~/.claude/skills/

# 3. ¡Ya está! Claude lo usará automáticamente
```

📖 **[Ver Guía de Inicio Rápido Completa →](QUICKSTART.md)**

## 🎯 ¿Qué son Agent Skills?

Los Agent Skills son recursos modulares basados en el sistema de archivos que proporcionan a Claude expertise específico de dominio: workflows, contexto y mejores prácticas que transforman agentes de propósito general en especialistas.

**Compatibles con**: React, TypeScript, Angular, Python, Java, Kotlin | **Integración**: GitHub Copilot

## 📋 Skills Disponibles

### 🔧 Technical Skills

#### 1. **Code Analysis** (`code-analysis`)
Analiza y revisa código con mejores prácticas de ingeniería de software.
- Análisis de calidad de código para React, Angular, Python, Java, Kotlin
- Detección de code smells específicos de tu stack
- Recomendaciones de mejora con ejemplos concretos
- Métricas de complejidad y mantenibilidad

#### 2. **Documentation** (`documentation`)
Genera y mantiene documentación técnica profesional.
- API documentation (REST, GraphQL, gRPC)
- README files y guías de contribución
- Arquitectura de sistemas (diagramas, ADRs)
- Guías de usuario y onboarding

#### 3. **Testing** (`testing`)
Crea y ejecuta estrategias completas de testing.
- Unit tests (Jest, pytest, JUnit, Kotlin Test)
- Integration tests y E2E
- React Testing Library para componentes
- Test-driven development (TDD)
- Coverage analysis y mejora

#### 4. **Architecture** (`architecture`)
Diseña y evalúa arquitecturas de software.
- Patrones de diseño (SOLID, DDD, Clean Architecture)
- Arquitecturas de sistemas (microservicios, event-driven)
- Diagramas técnicos (C4 model, UML)
- Trade-off analysis y decisiones arquitectónicas

#### 5. **Refactoring** (`refactoring`)
Mejora código existente manteniendo su funcionalidad.
- Code modernization para React hooks, Kotlin coroutines
- Pattern implementation (Repository, Factory, Strategy)
- Performance optimization
- Reducción de deuda técnica

### 💼 Non-Technical Skills

#### 6. **Product Owner** (`product-owner`)
Gestión de producto, backlog y stakeholders.
- User stories y acceptance criteria
- Backlog prioritization (MoSCoW, RICE)
- Sprint planning y roadmaps
- Stakeholder communication

#### 7. **Engineering Manager** (`engineering-manager`)
Liderazgo técnico y gestión de equipos.
- 1-on-1s y career development
- Performance reviews
- Hiring y onboarding
- Team culture building

#### 8. **Human Resources** (`human-resources`)
Gestión de talento y operaciones de HR.
- Recruiting y candidate evaluation
- Employee engagement programs
- HR policies y compliance
- Onboarding (30-60-90 day plans)

#### 9. **Marketing** (`marketing`)
Campañas, contenido y estrategia de marketing.
- Content marketing (blog posts, case studies)
- SEO strategy y keyword research
- Social media campaigns
- Analytics y performance tracking

#### 10. **Communications** (`communications`)
Comunicación interna, externa y crisis.
- Internal comms (all-hands, newsletters)
- Press releases y media relations
- Crisis communication plans
- Executive communications

## 🚀 Cómo Usar

### En Claude API

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Subir el skill
with open("code-analysis.zip", "rb") as f:
    skill = client.skills.create(
        file=f,
        name="code-analysis"
    )

# Usar en una conversación
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
        "content": "Analiza el código en main.py"
    }],
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "files-api-2025-04-14"
    ]
)
```

### En Claude Code

1. Copia el directorio del skill a tu proyecto:
```bash
cp -r skills/code-analysis .claude/skills/
```

2. Claude descubrirá y usará el skill automáticamente

### En Claude.ai

1. Comprime el directorio del skill en un archivo ZIP
2. Ve a Settings > Features
3. Sube el archivo ZIP

## 📁 Estructura de un Skill

```
skill-name/
├── SKILL.md              # Instrucciones principales (requerido)
├── EXAMPLES.md           # Ejemplos de uso
├── REFERENCE.md          # Documentación detallada
├── scripts/              # Scripts auxiliares
│   ├── analyze.py
│   └── validate.py
└── templates/            # Plantillas y recursos
    └── template.json
```

### Niveles de Carga

1. **Metadata (siempre cargado)**: Frontmatter YAML con name y description
2. **Instrucciones (al activarse)**: Contenido principal de SKILL.md
3. **Recursos (bajo demanda)**: Archivos adicionales referenciados

## 🛠️ Desarrollo

### Crear un Nuevo Skill

1. Crea un directorio con el nombre del skill (lowercase, hyphens)
2. Crea `SKILL.md` con frontmatter:
```markdown
---
name: mi-skill
description: Descripción clara de qué hace y cuándo usarlo
---

# Mi Skill

## Quick Start
[Instrucciones básicas]

## Workflows
[Procedimientos paso a paso]

## Examples
[Ejemplos concretos]
```

3. Añade recursos adicionales según necesidad

### Mejores Prácticas

- **Descripción clara**: Incluye qué hace Y cuándo usarlo
- **Instrucciones específicas**: Paso a paso, sin ambigüedad
- **Ejemplos concretos**: Casos de uso reales
- **Scripts para operaciones determinísticas**: Reduce consumo de tokens
- **Progressive disclosure**: Solo carga lo necesario

## 📊 Beneficios

✅ **Especialización**: Adapta capacidades para tareas específicas
✅ **Sin repetición**: Crea una vez, usa automáticamente
✅ **Composición**: Combina Skills para workflows complejos
✅ **Eficiencia de contexto**: Carga bajo demanda
✅ **Código reutilizable**: Scripts ejecutables sin consumir tokens

## 🔒 Seguridad

⚠️ **Usa solo Skills de fuentes confiables**:
- Skills propios
- Skills oficiales de Anthropic
- Audita completamente skills de terceros

Los Skills pueden ejecutar código y acceder a archivos. Tratalos como instalar software.

## 📚 Documentación

### 📖 Guías del Proyecto
- **[🚀 Quick Start](QUICKSTART.md)** - ¡Empieza en 5 minutos!
- **[📘 Guía de Uso](USAGE_GUIDE.md)** - Uso detallado en cada plataforma
- **[📋 Estructura](STRUCTURE.md)** - Organización del proyecto
- **[🤝 Contribuir](CONTRIBUTING.md)** - Cómo contribuir nuevos skills

### 🔗 Referencias Oficiales
- [Documentación oficial de Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)

## 📄 Licencia

MIT License - Ver archivo LICENSE para detalles

---

**Nota**: Esta colección sigue las especificaciones oficiales de Anthropic para Agent Skills y es compatible con Claude API, Claude Code, y Claude.ai.
