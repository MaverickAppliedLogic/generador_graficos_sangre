# Proyecto de Gestión y Análisis de Pacientes

Pequeño programa Python que implementa un sistema de **captura, validación, normalización y visualización de datos clínicos de pacientes**.

## Funcionalidad principal

- **Captura interactiva de datos**  
  Se solicitan al usuario los datos personales (nombre, género, dirección, teléfono) y parámetros clínicos (hemograma y perfil lipídico) de cada paciente.

- **Validación y normalización**  
  - Los datos se validan mediante la clase `Validador` (rangos y formatos correctos).  
  - Se normalizan con `NormalizadorDatos` para ajustar valores clínicos a rangos estándar.

- **Gestión de pacientes**  
  - Los pacientes se almacenan en una lista gestionada por `gestorPacientes`.  
  - Se pueden recuperar, actualizar y mantener organizados.

- **Visualización**  
  - Se generan gráficos comparativos (original vs normalizado) con `modeladorGraficos`.  
  - Se muestran distribuciones de los parámetros sanguíneos de los 30 pacientes capturados.

## Flujo del programa

1. El usuario introduce los datos de **30 pacientes** mediante la función `obtener_datos()`.  
2. Los pacientes se agregan al gestor (`gp.agregar_paciente`).  
3. Se construye un **DataFrame** con los datos originales.  
4. Se normalizan todos los pacientes y se genera un segundo **DataFrame** con los datos ajustados.  
5. Se imprimen ambos conjuntos en consola (sin normalizar vs normalizados).  
6. Se generan gráficos comparativos para visualizar las diferencias.

## Objetivo

El programa permite **simular y analizar distribuciones de valores sanguíneos**, mostrando cómo la normalización afecta los datos clínicos. Es una herramienta didáctica para comprender:

- Validación de datos médicos.  
- Normalización de parámetros clínicos.  
- Uso de pandas y gráficos para análisis comparativo.

---
