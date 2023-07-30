public class A71_ClassRetangulo {
    private double base;
    private double altura;

    // Construtor padrão
    public A71_ClassRetangulo() {
        base = 2;
        altura = 1;
    }

    // Construtor com base e altura
    public A71_ClassRetangulo (double b, double a) {
        base = b;
        altura = a;
    }

    // Get e Set para a base
    public double getBase() {
        return base;
    }

    public void setBase(double b) {
        base = b;
    }

    // Get e Set para a altura
    public double getAltura() {
        return altura;
    }

    public void setAltura(double a) {
        altura = a;
    }

    // Método para calcular a área do retângulo
    public double calcularArea() {
        return base * altura;
    }

    // Método para calcular o perímetro do retângulo
    public double calcularPerimetro() {
        return 2 * (base + altura);
    }

    // Método para verificar se o objeto é um quadrado
    public boolean ehQuadrado() {
        return base == altura;
    }

    // Método para imprimir todas as informações sobre o objeto
    public void verDados() {
        System.out.println("Base: " + base);
        System.out.println("Altura: " + altura);
        System.out.println("Area: " + calcularArea());
        System.out.println("Perimetro: " + calcularPerimetro());
        System.out.println("E um quadrado? " + ehQuadrado());
    }
}