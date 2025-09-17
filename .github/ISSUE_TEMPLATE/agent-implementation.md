---
name: 🤖 Agent Implementation Request
about: Request implementation of a new agent pattern
title: "[Agent] Implement [Agent Name] - [Brief Description]"
labels: ["agent-implementation", "enhancement", "help wanted"]
assignees: ""
---

## 🎯 **Agent Overview**

**Agent Name:** [e.g., Weather Agent, Code Review Agent]
**Category:** [Basic/Tool-Using/Memory-State/Reasoning/Multi-Agent/Specialized/Advanced]
**Complexity Level:** [⭐ to ⭐⭐⭐⭐⭐]

## 📋 **Agent Specification**

### **Purpose**

What problem does this agent solve? What is its primary function?

### **Core Capabilities**

- [ ] Capability 1 (e.g., Parse natural language queries)
- [ ] Capability 2 (e.g., Integrate with external weather API)
- [ ] Capability 3 (e.g., Format responses in multiple formats)

### **Input/Output Format**

**Input:**

```python
# Example input format
{
    "query": "What's the weather in New York?",
    "format": "detailed",
    "units": "metric"
}
```

**Output:**

```python
# Example output format
{
    "status": "success",
    "data": {
        "temperature": 22,
        "conditions": "sunny",
        "forecast": [...]
    },
    "metadata": {
        "timestamp": "2024-01-01T12:00:00Z",
        "source": "openweathermap"
    }
}
```

## 🔧 **Technical Requirements**

### **Dependencies**

- [ ] External APIs (specify which ones)
- [ ] Python packages (list required packages)
- [ ] Environment variables (list required config)
- [ ] Hardware requirements (if any)

### **Integration Points**

- [ ] Database connections needed
- [ ] File system access required
- [ ] Network permissions required
- [ ] Authentication mechanisms

## 🎯 **Acceptance Criteria**

### **Functional Requirements**

- [ ] Agent processes valid inputs correctly
- [ ] Agent handles invalid inputs gracefully
- [ ] Agent integrates with specified external services
- [ ] Agent returns consistent output format
- [ ] Agent includes proper error handling

### **Non-Functional Requirements**

- [ ] Response time < 5 seconds for typical requests
- [ ] Memory usage < 100MB during operation
- [ ] Handles concurrent requests (if applicable)
- [ ] Includes comprehensive logging
- [ ] Follows security best practices

### **Documentation Requirements**

- [ ] README.md with usage examples
- [ ] API documentation
- [ ] Configuration guide
- [ ] Troubleshooting section
- [ ] Performance benchmarks

### **Testing Requirements**

- [ ] Unit tests (>80% coverage)
- [ ] Integration tests
- [ ] Error handling tests
- [ ] Performance tests
- [ ] End-to-end examples

## 📚 **Reference Materials**

### **Similar Implementations**

- Link to similar agents in other repositories
- Academic papers or research
- Industry best practices

### **API Documentation**

- Links to external service documentation
- Authentication guides
- Rate limiting information

## 🌟 **Implementation Ideas**

### **Basic Implementation**

Describe the minimal viable implementation approach.

### **Advanced Features** (Optional)

- [ ] Caching mechanisms
- [ ] Retry logic with exponential backoff
- [ ] Multiple data source integration
- [ ] Real-time streaming capabilities
- [ ] Machine learning enhancements

## 👥 **Collaboration**

### **Skills Needed**

- [ ] Python programming
- [ ] API integration
- [ ] Testing frameworks
- [ ] Documentation writing
- [ ] Domain expertise (specify domain)

### **Mentorship Available**

- [ ] I can provide mentorship for this implementation
- [ ] I need mentorship for this implementation
- [ ] I can help with testing and review

### **Timeline**

**Estimated effort:** [1-5 hours / 1-2 days / 1-2 weeks / 1+ months]
**Target completion:** [Date or "flexible"]

## 📝 **Additional Context**

Add any other context, screenshots, examples, or references that would help implementers understand the requirements.

---

## 🚀 **Ready to Implement?**

- [ ] I want to implement this agent
- [ ] I can help with testing and review
- [ ] I can provide domain expertise consultation
- [ ] I can help with documentation

**Comment below if you're interested in contributing to this agent implementation!**
