import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.*;
import java.util.stream.Collectors;

public class TaskManager {
    private List<Task> tasks;
    private List<Category> categories;
    private Scanner scanner;
    
    public TaskManager() {
        this.tasks = new ArrayList<>();
        this.categories = initializeCategories();
        this.scanner = new Scanner(System.in);
        
        // Adicionar algumas tarefas de exemplo
        initializeSampleTasks();
    }
    
    private List<Category> initializeCategories() {
        List<Category> cats = new ArrayList<>();
        cats.add(new Category("work", "Trabalho", "blue", "💼"));
        cats.add(new Category("personal", "Pessoal", "green", "🏠"));
        cats.add(new Category("health", "Saúde", "red", "❤️"));
        cats.add(new Category("study", "Estudos", "purple", "📚"));
        cats.add(new Category("shopping", "Compras", "yellow", "🛒"));
        cats.add(new Category("travel", "Viagem", "indigo", "✈️"));
        return cats;
    }
    
    private void initializeSampleTasks() {
        // Adicionar tarefas de exemplo
        tasks.add(new Task("Revisar relatório mensal", "Analisar dados de vendas e preparar apresentação", 
                          Task.Priority.HIGH, "work", LocalDateTime.now().plusDays(2)));
        
        tasks.add(new Task("Consulta médica", "Consulta de rotina com cardiologista", 
                          Task.Priority.MEDIUM, "health", LocalDateTime.now().plusDays(5)));
        
        tasks.add(new Task("Estudar Java", "Completar módulo de Collections", 
                          Task.Priority.MEDIUM, "study"));
        
        tasks.add(new Task("Comprar ingredientes", "Lista: tomate, cebola, alho, azeite", 
                          Task.Priority.LOW, "shopping", LocalDateTime.now().plusDays(1)));
        
        // Marcar uma como concluída
        tasks.get(2).setCompleted(true);
    }
    
    public void run() {
        System.out.println("🚀 Bem-vindo à Agenda Moderna em Java!");
        System.out.println("Organize suas tarefas com eficiência e estilo.\n");
        
        while (true) {
            showMainMenu();
            int choice = getIntInput("Escolha uma opção: ");
            
            switch (choice) {
                case 1:
                    showDashboard();
                    break;
                case 2:
                    addNewTask();
                    break;
                case 3:
                    listTasks();
                    break;
                case 4:
                    searchTasks();
                    break;
                case 5:
                    editTask();
                    break;
                case 6:
                    deleteTask();
                    break;
                case 7:
                    toggleTaskStatus();
                    break;
                case 8:
                    showStatistics();
                    break;
                case 9:
                    showCategories();
                    break;
                case 0:
                    System.out.println("👋 Obrigado por usar a Agenda Moderna! Até logo!");
                    return;
                default:
                    System.out.println("❌ Opção inválida! Tente novamente.");
            }
            
            System.out.println("\nPressione Enter para continuar...");
            scanner.nextLine();
        }
    }
    
    private void showMainMenu() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("📋 AGENDA MODERNA - MENU PRINCIPAL");
        System.out.println("=".repeat(60));
        System.out.println("1. 📊 Dashboard");
        System.out.println("2. ➕ Adicionar Nova Tarefa");
        System.out.println("3. 📝 Listar Todas as Tarefas");
        System.out.println("4. 🔍 Pesquisar Tarefas");
        System.out.println("5. ✏️  Editar Tarefa");
        System.out.println("6. 🗑️  Excluir Tarefa");
        System.out.println("7. ✅ Marcar/Desmarcar Tarefa");
        System.out.println("8. 📈 Estatísticas");
        System.out.println("9. 📂 Categorias");
        System.out.println("0. 🚪 Sair");
        System.out.println("=".repeat(60));
    }
    
    private void showDashboard() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("📊 DASHBOARD - VISÃO GERAL");
        System.out.println("=".repeat(60));
        
        TaskStatistics stats = new TaskStatistics(tasks);
        stats.printStatistics();
        
        System.out.println("\n🔥 TAREFAS PRIORITÁRIAS:");
        List<Task> highPriorityTasks = tasks.stream()
                .filter(task -> task.getPriority() == Task.Priority.HIGH)
                .filter(task -> !task.isCompleted())
                .limit(3)
                .collect(Collectors.toList());
        
        if (highPriorityTasks.isEmpty()) {
            System.out.println("   ✨ Nenhuma tarefa de alta prioridade pendente!");
        } else {
            for (int i = 0; i < highPriorityTasks.size(); i++) {
                Task task = highPriorityTasks.get(i);
                System.out.printf("   %d. %s %s\n", i + 1, 
                    task.isOverdue() ? "⚠️" : "🔴", task.getTitle());
            }
        }
        
        System.out.println("\n⏰ TAREFAS COM PRAZO PRÓXIMO:");
        List<Task> upcomingTasks = tasks.stream()
                .filter(task -> task.getDueDate() != null)
                .filter(task -> !task.isCompleted())
                .filter(task -> task.getDueDate().isAfter(LocalDateTime.now()))
                .filter(task -> task.getDueDate().isBefore(LocalDateTime.now().plusDays(7)))
                .sorted((t1, t2) -> t1.getDueDate().compareTo(t2.getDueDate()))
                .limit(3)
                .collect(Collectors.toList());
        
        if (upcomingTasks.isEmpty()) {
            System.out.println("   ✨ Nenhuma tarefa com prazo próximo!");
        } else {
            for (int i = 0; i < upcomingTasks.size(); i++) {
                Task task = upcomingTasks.get(i);
                System.out.printf("   %d. 📅 %s - %s\n", i + 1, 
                    task.getTitle(), task.getFormattedDueDate());
            }
        }
    }
    
    private void addNewTask() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("➕ ADICIONAR NOVA TAREFA");
        System.out.println("=".repeat(60));
        
        System.out.print("📝 Título da tarefa: ");
        String title = scanner.nextLine().trim();
        
        if (title.isEmpty()) {
            System.out.println("❌ O título não pode estar vazio!");
            return;
        }
        
        System.out.print("📄 Descrição (opcional): ");
        String description = scanner.nextLine().trim();
        if (description.isEmpty()) description = null;
        
        // Selecionar prioridade
        Task.Priority priority = selectPriority();
        
        // Selecionar categoria
        String category = selectCategory();
        
        // Data de vencimento
        LocalDateTime dueDate = selectDueDate();
        
        Task newTask = new Task(title, description, priority, category, dueDate);
        tasks.add(newTask);
        
        System.out.println("✅ Tarefa adicionada com sucesso!");
        System.out.println(newTask);
    }
    
    private Task.Priority selectPriority() {
        System.out.println("\n🏷️ Selecione a prioridade:");
        System.out.println("1. 🟢 Baixa");
        System.out.println("2. 🟡 Média");
        System.out.println("3. 🔴 Alta");
        
        int choice = getIntInput("Prioridade (1-3): ");
        switch (choice) {
            case 1: return Task.Priority.LOW;
            case 2: return Task.Priority.MEDIUM;
            case 3: return Task.Priority.HIGH;
            default: 
                System.out.println("⚠️ Opção inválida, usando prioridade média.");
                return Task.Priority.MEDIUM;
        }
    }
    
    private String selectCategory() {
        System.out.println("\n📂 Selecione a categoria:");
        for (int i = 0; i < categories.size(); i++) {
            System.out.printf("%d. %s\n", i + 1, categories.get(i));
        }
        
        int choice = getIntInput("Categoria (1-" + categories.size() + "): ");
        if (choice >= 1 && choice <= categories.size()) {
            return categories.get(choice - 1).getId();
        } else {
            System.out.println("⚠️ Opção inválida, usando categoria 'Pessoal'.");
            return "personal";
        }
    }
    
    private LocalDateTime selectDueDate() {
        System.out.print("📅 Data de vencimento (dd/MM/yyyy HH:mm) ou Enter para pular: ");
        String dateInput = scanner.nextLine().trim();
        
        if (dateInput.isEmpty()) {
            return null;
        }
        
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
            return LocalDateTime.parse(dateInput, formatter);
        } catch (DateTimeParseException e) {
            System.out.println("⚠️ Formato de data inválido, tarefa criada sem prazo.");
            return null;
        }
    }
    
    private void listTasks() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("📝 LISTA DE TAREFAS");
        System.out.println("=".repeat(60));
        
        if (tasks.isEmpty()) {
            System.out.println("📭 Nenhuma tarefa encontrada!");
            return;
        }
        
        System.out.println("Como deseja visualizar as tarefas?");
        System.out.println("1. 🔄 Ordem padrão (por prioridade)");
        System.out.println("2. 📅 Por data de vencimento");
        System.out.println("3. ✅ Concluídas primeiro");
        System.out.println("4. ⏳ Pendentes primeiro");
        
        int sortChoice = getIntInput("Escolha (1-4): ");
        List<Task> sortedTasks = new ArrayList<>(tasks);
        
        switch (sortChoice) {
            case 1:
                sortedTasks = TaskFilter.sortByPriority(tasks);
                break;
            case 2:
                sortedTasks = TaskFilter.sortByDueDate(tasks);
                break;
            case 3:
                sortedTasks = tasks.stream()
                    .sorted((t1, t2) -> Boolean.compare(t2.isCompleted(), t1.isCompleted()))
                    .collect(Collectors.toList());
                break;
            case 4:
                sortedTasks = tasks.stream()
                    .sorted((t1, t2) -> Boolean.compare(t1.isCompleted(), t2.isCompleted()))
                    .collect(Collectors.toList());
                break;
        }
        
        for (int i = 0; i < sortedTasks.size(); i++) {
            System.out.printf("\n📋 TAREFA #%d\n", i + 1);
            System.out.println(sortedTasks.get(i));
        }
    }
    
    private void searchTasks() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("🔍 PESQUISAR TAREFAS");
        System.out.println("=".repeat(60));
        
        System.out.print("🔎 Digite o termo de busca: ");
        String searchTerm = scanner.nextLine().trim();
        
        if (searchTerm.isEmpty()) {
            System.out.println("❌ Termo de busca não pode estar vazio!");
            return;
        }
        
        List<Task> filteredTasks = TaskFilter.filterTasks(tasks, searchTerm, null, null, null);
        
        if (filteredTasks.isEmpty()) {
            System.out.println("📭 Nenhuma tarefa encontrada com o termo: " + searchTerm);
            return;
        }
        
        System.out.printf("🎯 Encontradas %d tarefa(s):\n", filteredTasks.size());
        for (int i = 0; i < filteredTasks.size(); i++) {
            System.out.printf("\n📋 RESULTADO #%d\n", i + 1);
            System.out.println(filteredTasks.get(i));
        }
    }
    
    private void editTask() {
        if (tasks.isEmpty()) {
            System.out.println("📭 Nenhuma tarefa para editar!");
            return;
        }
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("✏️ EDITAR TAREFA");
        System.out.println("=".repeat(60));
        
        listTasksSimple();
        int index = getIntInput("Número da tarefa para editar: ") - 1;
        
        if (index < 0 || index >= tasks.size()) {
            System.out.println("❌ Número de tarefa inválido!");
            return;
        }
        
        Task task = tasks.get(index);
        System.out.println("\n📋 Tarefa atual:");
        System.out.println(task);
        
        System.out.println("\nO que deseja editar?");
        System.out.println("1. 📝 Título");
        System.out.println("2. 📄 Descrição");
        System.out.println("3. 🏷️ Prioridade");
        System.out.println("4. 📂 Categoria");
        System.out.println("5. 📅 Data de vencimento");
        System.out.println("0. ↩️ Voltar");
        
        int choice = getIntInput("Escolha: ");
        
        switch (choice) {
            case 1:
                System.out.print("Novo título: ");
                String newTitle = scanner.nextLine().trim();
                if (!newTitle.isEmpty()) {
                    task.setTitle(newTitle);
                    System.out.println("✅ Título atualizado!");
                }
                break;
            case 2:
                System.out.print("Nova descrição: ");
                String newDescription = scanner.nextLine().trim();
                task.setDescription(newDescription.isEmpty() ? null : newDescription);
                System.out.println("✅ Descrição atualizada!");
                break;
            case 3:
                task.setPriority(selectPriority());
                System.out.println("✅ Prioridade atualizada!");
                break;
            case 4:
                task.setCategory(selectCategory());
                System.out.println("✅ Categoria atualizada!");
                break;
            case 5:
                task.setDueDate(selectDueDate());
                System.out.println("✅ Data de vencimento atualizada!");
                break;
            case 0:
                return;
            default:
                System.out.println("❌ Opção inválida!");
        }
    }
    
    private void deleteTask() {
        if (tasks.isEmpty()) {
            System.out.println("📭 Nenhuma tarefa para excluir!");
            return;
        }
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("🗑️ EXCLUIR TAREFA");
        System.out.println("=".repeat(60));
        
        listTasksSimple();
        int index = getIntInput("Número da tarefa para excluir: ") - 1;
        
        if (index < 0 || index >= tasks.size()) {
            System.out.println("❌ Número de tarefa inválido!");
            return;
        }
        
        Task task = tasks.get(index);
        System.out.println("\n📋 Tarefa a ser excluída:");
        System.out.println(task);
        
        System.out.print("⚠️ Tem certeza que deseja excluir esta tarefa? (s/N): ");
        String confirmation = scanner.nextLine().trim().toLowerCase();
        
        if (confirmation.equals("s") || confirmation.equals("sim")) {
            tasks.remove(index);
            System.out.println("✅ Tarefa excluída com sucesso!");
        } else {
            System.out.println("❌ Operação cancelada.");
        }
    }
    
    private void toggleTaskStatus() {
        if (tasks.isEmpty()) {
            System.out.println("📭 Nenhuma tarefa disponível!");
            return;
        }
        
        System.out.println("\n" + "=".repeat(60));
        System.out.println("✅ MARCAR/DESMARCAR TAREFA");
        System.out.println("=".repeat(60));
        
        listTasksSimple();
        int index = getIntInput("Número da tarefa: ") - 1;
        
        if (index < 0 || index >= tasks.size()) {
            System.out.println("❌ Número de tarefa inválido!");
            return;
        }
        
        Task task = tasks.get(index);
        task.toggleCompleted();
        
        String status = task.isCompleted() ? "concluída" : "pendente";
        System.out.printf("✅ Tarefa marcada como %s!\n", status);
        System.out.println(task);
    }
    
    private void showStatistics() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("📈 ESTATÍSTICAS DETALHADAS");
        System.out.println("=".repeat(60));
        
        TaskStatistics stats = new TaskStatistics(tasks);
        stats.printStatistics();
        
        // Mostrar tarefas atrasadas se houver
        List<Task> overdueTasks = tasks.stream()
                .filter(Task::isOverdue)
                .collect(Collectors.toList());
        
        if (!overdueTasks.isEmpty()) {
            System.out.println("\n⚠️ TAREFAS ATRASADAS:");
            for (int i = 0; i < overdueTasks.size(); i++) {
                Task task = overdueTasks.get(i);
                System.out.printf("   %d. %s (Prazo: %s)\n", 
                    i + 1, task.getTitle(), task.getFormattedDueDate());
            }
        }
    }
    
    private void showCategories() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("📂 CATEGORIAS DISPONÍVEIS");
        System.out.println("=".repeat(60));
        
        for (Category category : categories) {
            long taskCount = tasks.stream()
                    .filter(task -> task.getCategory().equals(category.getId()))
                    .count();
            
            System.out.printf("%s - %d tarefa(s)\n", category, taskCount);
        }
    }
    
    private void listTasksSimple() {
        System.out.println("\n📋 Lista de Tarefas:");
        for (int i = 0; i < tasks.size(); i++) {
            Task task = tasks.get(i);
            String status = task.isCompleted() ? "✅" : "⭕";
            String priority = task.getPriority() == Task.Priority.HIGH ? "🔴" : 
                            task.getPriority() == Task.Priority.MEDIUM ? "🟡" : "🟢";
            String overdue = task.isOverdue() ? " ⚠️" : "";
            
            System.out.printf("%d. %s %s %s%s\n", 
                i + 1, status, priority, task.getTitle(), overdue);
        }
    }
    
    private int getIntInput(String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                String input = scanner.nextLine().trim();
                return Integer.parseInt(input);
            } catch (NumberFormatException e) {
                System.out.println("❌ Por favor, digite um número válido!");
            }
        }
    }
    
    // Getters para acesso externo se necessário
    public List<Task> getTasks() {
        return new ArrayList<>(tasks);
    }
    
    public List<Category> getCategories() {
        return new ArrayList<>(categories);
    }
}
println("lock")
