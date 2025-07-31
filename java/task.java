import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

public class Task {
    private String id;
    private String title;
    private String description;
    private boolean completed;
    private Priority priority;
    private String category;
    private LocalDateTime dueDate;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    
    public enum Priority {
        LOW("Baixa"), MEDIUM("Média"), HIGH("Alta");
        
        private final String displayName;
        
        Priority(String displayName) {
            this.displayName = displayName;
        }
        
        public String getDisplayName() {
            return displayName;
        }
    }
    
    // Construtor
    public Task(String title, String description, Priority priority, String category, LocalDateTime dueDate) {
        this.id = UUID.randomUUID().toString();
        this.title = title;
        this.description = description;
        this.completed = false;
        this.priority = priority;
        this.category = category;
        this.dueDate = dueDate;
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
    }
    
    // Construtor simplificado
    public Task(String title, Priority priority, String category) {
        this(title, null, priority, category, null);
    }
    
    // Getters e Setters
    public String getId() { return id; }
    
    public String getTitle() { return title; }
    public void setTitle(String title) { 
        this.title = title; 
        this.updatedAt = LocalDateTime.now();
    }
    
    public String getDescription() { return description; }
    public void setDescription(String description) { 
        this.description = description; 
        this.updatedAt = LocalDateTime.now();
    }
    
    public boolean isCompleted() { return completed; }
    public void setCompleted(boolean completed) { 
        this.completed = completed; 
        this.updatedAt = LocalDateTime.now();
    }
    
    public Priority getPriority() { return priority; }
    public void setPriority(Priority priority) { 
        this.priority = priority; 
        this.updatedAt = LocalDateTime.now();
    }
    
    public String getCategory() { return category; }
    public void setCategory(String category) { 
        this.category = category; 
        this.updatedAt = LocalDateTime.now();
    }
    
    public LocalDateTime getDueDate() { return dueDate; }
    public void setDueDate(LocalDateTime dueDate) { 
        this.dueDate = dueDate; 
        this.updatedAt = LocalDateTime.now();
    }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    
    // Métodos utilitários
    public boolean isOverdue() {
        return dueDate != null && LocalDateTime.now().isAfter(dueDate) && !completed;
    }
    
    public String getFormattedDueDate() {
        if (dueDate == null) return "Sem prazo";
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        return dueDate.format(formatter);
    }
    
    public String getFormattedCreatedAt() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");
        return createdAt.format(formatter);
    }
    
    public void toggleCompleted() {
        this.completed = !this.completed;
        this.updatedAt = LocalDateTime.now();
    }
    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("┌─────────────────────────────────────────────────────────────┐\n");
        sb.append(String.format("│ %-59s │\n", (completed ? "✅ " : "⭕ ") + title));
        sb.append("├─────────────────────────────────────────────────────────────┤\n");
        
        if (description != null && !description.trim().isEmpty()) {
            sb.append(String.format("│ Descrição: %-48s │\n", description));
        }
        
        sb.append(String.format("│ Prioridade: %-47s │\n", getPriorityIcon() + " " + priority.getDisplayName()));
        sb.append(String.format("│ Categoria: %-48s │\n", category));
        sb.append(String.format("│ Prazo: %-52s │\n", getFormattedDueDate()));
        sb.append(String.format("│ Criada em: %-47s │\n", getFormattedCreatedAt()));
        
        if (isOverdue()) {
            sb.append("│ ⚠️  TAREFA ATRASADA!                                      │\n");
        }
        
        sb.append("└─────────────────────────────────────────────────────────────┘");
        return sb.toString();
    }
    
    private String getPriorityIcon() {
        switch (priority) {
            case HIGH: return "🔴";
            case MEDIUM: return "🟡";
            case LOW: return "🟢";
            default: return "⚪";
        }
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Task task = (Task) obj;
        return id.equals(task.id);
    }
    
    @Override
    public int hashCode() {
        return id.hashCode();
    }
}
