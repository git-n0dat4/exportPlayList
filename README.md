# Export Spotify Playlist
Este script de Python exporta las canciones de una lista de reproducción de Spotify a un archivo de texto, agrupándolas por artista.

## Cómo usar
- Para usar este script, necesitarás un `client_id` y un `client_secret` de Spotify. Puedes obtener estos creando una aplicación en el Dashboard de Desarrolladores de Spotify.
- Una vez que tengas tu `client_id` y `client_secret`, reemplaza las cadenas de texto `client_id` y `client_secret` en la función `main()` con tus credenciales.
- También necesitarás proporcionar la URL de la lista de reproducción de Spotify que quieres exportar. Reemplaza la cadena de texto `playlist_url` en la función `main()` con la URL de tu lista de reproducción.
- Finalmente, puedes especificar el nombre del archivo de texto al que se exportarán las canciones reemplazando la cadena de texto `filename.txt` en la función `main()` con el nombre de archivo que prefieras.
