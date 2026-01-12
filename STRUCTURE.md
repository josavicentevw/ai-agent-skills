# Estructura del Proyecto AI Agent Skills

```
ai-agent-skills/
│
├── 📄 README.md                    # Documentación principal del proyecto
├── 📄 LICENSE                      # Licencia MIT
├── 📄 CONTRIBUTING.md              # Guía para contribuir
├── 📄 USAGE_GUIDE.md              # Guía de uso detallada
├── 📄 .gitignore                  # Archivos ignorados por Git
├── 🔧 package-skills.sh           # Script para empaquetar skills
│
├── 📁 examples/                    # Ejemplos de uso
│   └── api_example.py             # Ejemplo de uso con Claude API
│
└── 📁 skills/                      # Directorio de skills
    │
    ├── 📁 code-analysis/           # Skill de análisis de código
    │   ├── SKILL.md               # ⭐ Archivo principal del skill
    │   ├── EXAMPLES.md            # Ejemplos detallados
    │   └── scripts/
    │       └── analyze.py         # Script de análisis Python
    │
    ├── 📁 documentation/           # Skill de documentación
    │   └── SKILL.md               # ⭐ Archivo principal del skill
    │
    ├── 📁 testing/                 # Skill de testing
    │   └── SKILL.md               # ⭐ Archivo principal del skill
    │
    ├── 📁 architecture/            # Skill de arquitectura
    │   └── SKILL.md               # ⭐ Archivo principal del skill
    │
    └── 📁 refactoring/             # Skill de refactoring
        └── SKILL.md               # ⭐ Archivo principal del skill
```

## 🎯 Skills Creados

### 1. **code-analysis** 
Análisis de calidad de código, detección de code smells y métricas
- ✅ SKILL.md completo con guías detalladas
- ✅ EXAMPLES.md con ejemplos en Python, JavaScript, Java y Go
- ✅ Script analyze.py funcional para análisis automático

### 2. **documentation**
Generación de documentación técnica profesional
- ✅ Templates para README, API docs, ADRs
- ✅ Estándares de documentación (Google, JSDoc, Javadoc)
- ✅ Guías para múltiples tipos de documentación

### 3. **testing**
Creación de tests unitarios e integración
- ✅ Patrones de testing (AAA, Given-When-Then)
- ✅ Ejemplos con pytest, Jest, JUnit
- ✅ Guías de TDD y cobertura

### 4. **architecture**
Diseño y evaluación de arquitecturas de software
- ✅ Patrones arquitectónicos (microservicios, event-driven, etc.)
- ✅ Diagramas y decisiones de arquitectura
- ✅ Guías de escalabilidad y selección de tecnología

### 5. **refactoring**
Mejora de código existente manteniendo funcionalidad
- ✅ Catálogo de refactorings
- ✅ Técnicas de modernización de código
- ✅ Patrones de migración incremental

## 📦 Cómo Usar

### 1. Empaquetar Skills
```bash
./package-skills.sh
# Crea ZIPs en packaged-skills/
```

### 2. Usar con Claude API
```python
import anthropic
client = anthropic.Anthropic(api_key="tu-key")

with open("packaged-skills/code-analysis.zip", "rb") as f:
    skill = client.skills.create(file=f, name="code-analysis")
```

### 3. Usar con Claude Code
```bash
cp -r skills/code-analysis ~/.claude/skills/
```

### 4. Usar con Claude.ai
- Settings > Features > Upload Skill
- Selecciona el ZIP del skill

## 🚀 Características

✅ **5 Skills profesionales completos**
✅ **Siguiendo especificaciones oficiales de Anthropic**
✅ **Documentación exhaustiva en español**
✅ **Ejemplos de código en múltiples lenguajes**
✅ **Scripts ejecutables incluidos**
✅ **Guías de contribución y uso**
✅ **Listo para producción**

## 📚 Documentación

- `README.md` - Overview y features
- `USAGE_GUIDE.md` - Guía paso a paso
- `CONTRIBUTING.md` - Cómo contribuir
- Cada skill tiene `SKILL.md` con documentación completa

## 🔧 Herramientas

- `package-skills.sh` - Empaqueta skills como ZIP
- `examples/api_example.py` - Ejemplo de integración con API
- `skills/code-analysis/scripts/analyze.py` - Análisis automático

## 🎓 Basado en

- [Anthropic Agent Skills Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
- [Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

---

**Listo para usar!** 🎉
