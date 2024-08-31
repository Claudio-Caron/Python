List<int> BinaryConverter(int number){
    List<int> lista = new List<int>();
    List<int> retorno = new List<int>();
    List
    while(number > 1)
    {
        if (number%2==1)
        {
            lista.add(0);
        }else{
            lista.add(1);
        }
        number /=2;
    }
    for (int i = 0;i<lista.Count; i++)
    {
        retorno.add(lista(i));
    }
    return retorno;
} 
public static void main(String[] args){
    Console.WriteLine(BinaryConverter());
}