/**
 * Created by admin on 2017/12/11.
 */
function checkaction(v){
    if(v==0){
        document.register.action="../dele/?id={{ device_info.id }}";
    }else if(v==1){
        document.register.action="../choose/?id={{ device_info.id }}";
    }else{
        document.register.action="../result/";
    }
    register.submit();
}
