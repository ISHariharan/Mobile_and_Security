import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.security.SecureRandom;
import java.util.Base64;

public class Des {
    private static final String ALGORITHM = "DES";
    private static final int KEY_SIZE = 56;

    public static void main(String[] args) throws Exception {
        KeyGenerator keyGen = KeyGenerator.getInstance(ALGORITHM);
        keyGen.init(KEY_SIZE);
        SecretKey key = keyGen.generateKey();
        byte[] keyValue = key.getEncoded();
        System.out.println("Key: " + Base64.getEncoder().encodeToString(keyValue));
        String message = "Hello, World!";
        byte[] encrypted = encrypt(message, keyValue);
        System.out.println("Encrypted: " + Base64.getEncoder().encodeToString(encrypted));
        byte[] decrypted = decrypt(encrypted, keyValue);
        System.out.println("Decrypted: " + new String(decrypted));
    }

    public static byte[] encrypt(String message, byte[] keyValue) throws Exception {
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(keyValue, ALGORITHM));
        return cipher.doFinal(message.getBytes());
    }

    public static byte[] decrypt(byte[] encrypted, byte[] keyValue) throws Exception {
        Cipher cipher = Cipher.getInstance(ALGORITHM);
        cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(keyValue, ALGORITHM));
        return cipher.doFinal(encrypted);
    }
}