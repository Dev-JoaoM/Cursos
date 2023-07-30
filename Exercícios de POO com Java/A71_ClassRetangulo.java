public class A71_ClassRetangulo {
    private double base;
    private double altura;

    // Construtor padr�o
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

    // M�todo para calcular a �rea do ret�ngulo
    public double calcularArea() {
        return base * altura;
    }

    // M�todo para calcular o per�metro do ret�ngulo
    public double calcularPerimetro() {
        return 2 * (base + altura);
    }

    // M�todo para verificar se o objeto � um quadrado
    public boolean ehQuadrado() {
        return base == altura;
    }

    // M�todo para imprimir todas as informa��es sobre o objeto
    public void verDados() {
        System.out.println("Base: " + base);
        System.out.println("Altura: " + altura);
        System.out.println("Area: " + calcularArea());
        System.out.println("Perimetro: " + calcularPerimetro());
        System.out.println("E um quadrado? " + ehQuadrado());
    }
}