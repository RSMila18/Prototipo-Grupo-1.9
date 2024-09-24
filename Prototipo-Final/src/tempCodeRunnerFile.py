    self.limpiar_frame()
        if self.usuario_actual:  # Verificar si hay un usuario actual
            historial = HistorialSolicitudes(self, self.usuario_actual)  # Agrega self.usuario_actual aquí
            historial.mostrar_historial()
        else:
            messagebox.showwarning("Advertencia", "Inicie sesión para ver su historial.")