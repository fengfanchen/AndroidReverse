package com.example.crakdemo2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final EditText retText = (EditText)findViewById(R.id.numEditText);
        Button okBtn = (Button)findViewById(R.id.okButton);
        okBtn.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {

                boolean ret = MyJni.isOk(retText.getText().toString());
                if(ret){

                    Toast.makeText(MainActivity.this, "失败", Toast.LENGTH_SHORT).show();
                }
                else{

                    Toast.makeText(MainActivity.this, R.string.successed, Toast.LENGTH_SHORT).show();
                }
            }

        });
    }
}
