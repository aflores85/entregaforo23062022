
<template>
  <div>
 
  <header style="text-align:center;">
  <hola-mundo-comp></hola-mundo-comp>
  </header>
    <h2> Dar de alta Foro </h2>
  <form-foro></form-foro>
  <h3> Dar de alta Tema en el Foro </h3>
  <Form-Subject></Form-Subject>
  <h4> Dar de alta un Posts en un tema </h4>
  <form-posts></form-posts>

  <div>
    <lista-foros></lista-foros>
  </div>
  
  <div>
    <Lista-Subject></Lista-Subject>
  </div>
  
  <div>
    <Lista-Posts></Lista-Posts>  
  </div>

  <div>
    <Contacto></Contacto>  
  </div>
  
</div>
  


</template>


<script>
import HolaMundoComp from "../components/HolaMundoComp";
import ListaForos from "../components/ListaForos";
import FormForo from "../components/FormForo";
import FormSubject from "../components/FormSubject";
import ListaSubject from "../components/ListaSubject";
import Contacto from "../components/Contacto";
import ListaPosts from "../components/ListaPosts";
import FormPosts from "../components/FormPosts";





export default {
  name: "InicioView",
  components: { HolaMundoComp, ListaForos, FormForo, FormSubject, ListaSubject, Contacto, ListaPosts, FormPosts },
    
};
</script>

<style scoped></style>

