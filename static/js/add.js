/**
 * Created by admin on 2017/12/11.
 */


function checkaction(v){
    if(v==0){
        document.register.action="../add/";
    }else{
        document.register.action="../list/";
    }
    register.submit();
}