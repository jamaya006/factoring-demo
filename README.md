# Sistema de Toma Física de Activos

## Arranque rápido
1. Copiar variables:
   ```bash
   cp .env.example .env
   ```
2. Levantar servicios:
   ```bash
   docker compose up --build
   ```
3. Crear superusuario:
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```
4. Acceder en red local:
   - `http://IP_VM:8000`

## Flujo recomendado MVP
1. Crear proyecto.
2. Cargar maestro Excel (hojas INC 1 e INC 2).
3. Ejecutar captura móvil desde `/inventory/takes/capture/`.
4. Correr conciliación por proyecto.
5. Exportar reporte final en XLSX.
