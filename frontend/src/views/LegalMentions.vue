<template>
  <v-main>
    <v-container>
      <h3>Personne morale</h3>
        <p>Marion Giusti <br>
        m.giusti9@gmail.com</p>
        <hr class="divider light my-4" />

        <h3>Auteur du site</h3>
        <p>Marion Giusti - Github</p>
          <a
            href="https://github.com/MarionGiusti/P13_MissionTriton"
            target="_blank"
          >
            <v-avatar class="mx-2" size="56">
              <img src="../assets/github.png" />
            </v-avatar>
          </a>
        <hr class="divider light my-4" />

      <h3>Coordonnées de l'hébergeur</h3>
        <p>Digital Ocean - Datacenter Amsterdam</p>
          <a
            href="https://cloud.digitalocean.com/"
            target="_blank"
          >
            <v-avatar class="mx-2" size="80">
              <v-img src="../assets/digitalocean-logo.png" height="50"/>
            </v-avatar>
          </a>
        <hr class="divider light my-4" />

      <h3>Ressources libres utilisées</h3>
        <p>Logo : Conception graphique logotype ©Justine Monchecourt</p>
        <p>Photos : Images libres de droit tirées de site comme Pixabay, Unsplash</p>
    </v-container>
  </v-main>
</template>

<script>
export default {
  name: "LegalMentions"
};
</script>
