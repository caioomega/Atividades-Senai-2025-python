public class Category {
    private String id;
    private String name;
    private String color;
    private String icon;
    
    public Category(String id, String name, String color, String icon) {
        this.id = id;
        this.name = name;
        this.color = color;
        this.icon = icon;
    }
    
    public String getId() { return id; }
    public String getName() { return name; }
    public String getColor() { return color; }
    public String getIcon() { return icon; }
    public String getCategory() { return opcional;}
    
    @Override
    public String toString() {
        return icon + " " + name;
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Category category = (Category) obj;
        return id.equals(category.id);
    }
    
    @Override
    public int hashCode() {
        return id.hashCode();
    }
}
