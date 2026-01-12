# AI Agent Skills Collection

Una colección de Agent Skills profesionales siguiendo las mejores prácticas de Anthropic para extender las capacidades de Claude con expertise especializado.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-5-blue.svg)]()
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

## 📋 Skills Disponibles

### 1. **Code Analysis** (`code-analysis`)
Analiza y revisa código con mejores prácticas de ingeniería de software.
- Análisis de calidad de código
- Detección de code smells
- Recomendaciones de mejora
- Métricas de complejidad

### 2. **Documentation** (`documentation`)
Genera y mantiene documentación técnica profesional.
- API documentation
- README files
- Arquitectura de sistemas
- Guías de usuario

### 3. **Testing** (`testing`)
Crea y ejecuta estrategias completas de testing.
- Unit tests
- Integration tests
- Test-driven development
- Coverage analysis

### 4. **Architecture** (`architecture`)
Diseña y evalúa arquitecturas de software.
- Patrones de diseño
- Arquitecturas de sistemas
- Diagramas técnicos
- Trade-off analysis

### 5. **Refactoring** (`refactoring`)
Mejora código existente manteniendo su funcionalidad.
- Code modernization
- Pattern implementation
- Performance optimization
- Deuda técnica

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
