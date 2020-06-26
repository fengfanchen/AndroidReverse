package com.example.crakdemo1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;



public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText eidt_userName = (EditText)findViewById(R.id.userName);
        final EditText eidt_sn = (EditText)findViewById(R.id.password);
        Button btn_register = (Button)findViewById(R.id.button);
        btn_register.setOnClickListener(new View.OnClickListener() {


            @Override
            public void onClick(View view) {

                if(!checkSN(eidt_userName.getText().toString().trim(), eidt_sn.getText().toString().trim())){

                    Toast.makeText(MainActivity.this, R.string.unsuccessed, Toast.LENGTH_SHORT).show();
                }
                else{

                    Toast.makeText(MainActivity.this, R.string.successed, Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    public static String bytesToHex(byte[] bytes) {
        StringBuilder buf = new StringBuilder(bytes.length * 2);
        for(byte b : bytes) { // 使用String的format方法进行转换
            buf.append(String.format("%02x", new Integer(b & 0xff)));
        }

        return buf.toString();
    }


    private boolean checkSN(String userName, String sn){

        try {

            if((userName == null) || (userName.length() == 0)){

                return false;
            }
            if((sn == null)){

                return false;
            }

            MessageDigest digest = MessageDigest.getInstance("MD5");
            digest.reset();
            digest.update(userName.getBytes());
            byte[] bytes = digest.digest();
            String hexStr = bytesToHex(bytes);
            StringBuffer sb = new StringBuffer();
            for(int i = 0; i < hexStr.length(); i+=2){

                sb.append(hexStr.charAt(i));
            }

            String userSN = sb.toString();

            if(!userSN.equalsIgnoreCase(sn)){

                return false;
            }
        }
        catch (NoSuchAlgorithmException e){

            e.printStackTrace();
            return false;
        }

        return true;
    }
}
