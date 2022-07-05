
<template>
  <div>

<header style="text-align:center;">

<hola-mundo-comp></hola-mundo-comp>

</header>
<table bordercolor = "#999933" border="8" cellpadding="1" cellspacing="1" tyle="width:100%"> 
  <tr>
  <td><h2> Dar de alta Foro </h2><form-foro></form-foro></td>
  <td><h3> Dar de alta Tema en el Foro </h3><Form-Subject></Form-Subject></td>
  <td> <h4> Dar de alta un Posts en un tema </h4><form-posts></form-posts></td>
 </tr>
</table>
<body>  

<table  style="width:100%"> 
  <tr>
  <td><div><lista-foros></lista-foros></div></td>
  <td><div><Lista-Subject></Lista-Subject></div></td>
  <td><div><Lista-Posts></Lista-Posts></div></td>
  </tr>
</table>
  
  <div><Contacto></Contacto></div>
 
 

</body>  
</div></template>


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
