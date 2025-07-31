public class AgendaApp {
    public static void main(String[] args) {
        try {
            System.setProperty("file.encoding", "UTF-8");
            
            TaskManager taskManager = new TaskManager();
            taskManager.run();
            
        } catch (Exception e) {
            System.err.println("❌ Erro inesperado na aplicação: " + e.getMessage());
            e.printStackTrace();
        }
    }
}

