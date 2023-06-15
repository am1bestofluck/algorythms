/**
 * Задание 1 (тайминг 5 минут)
Необходимо написать алгоритм, считающий сумму всех чисел
от 1 до N. Согласно свойствам линейной сложности,
количество итераций цикла будет линейно изменяться
относительно изменения размера N.
 */
public class one {

    public static void main(String[] args) {
        System.out.println(Counter(5));
    }

    public static int Counter(int number) {
        int result = 0;
        for (int i = 0; i <= number; i++) {
            result += i;
        }
        return result;
    }
}