import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;


public class Testes{

    App inst;

    @Before
    public void iniciar(){
        inst = new App();
    }

    @Test
    public void testes_Soma_simples(){
        assertEquals(inst.Soma(10,25),35);
    }

    @Test
    public void testes_Soma_complexa(){
        assertEquals(inst.Soma((-1), 12), 11);
    }

    @Test 
    public void Test_Subtracao_simples(){
        assertEquals(inst.Subtracao(100, 99), 1);
    }

    @Test 
    public void Test_Subtracao_complexa(){
        assertEquals(inst.Subtracao(50,(-50)), 100);
    }

}
