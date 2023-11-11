<template>
  <form @submit.prevent="enviarFormulario">
    <div class="mb-3">
      <label for="game" class="form-label">Jogo:</label>
      <select class="form-select" required v-model="jogoSelecionado" id="game">
        <option value="" selected>Selecione um jogo...</option>
        <option v-for="jogo in jogos" :value="jogo.sequence">{{ jogo.nome }}</option>
      </select>
      <label for="nome" class="form-label">Nome:</label>
      <input type="text" class="form-control" id="nome" required v-model="userName" />
    </div>
    <button type="submit" class="btn btn-primary">Enviar</button>
  </form>
</template>
  
<script>
import axios from 'axios'

export default {
  data() {
    return {
      userName: '',
      jogoSelecionado: '',
      jogos: []
    };
  },
  methods: {
    enviarFormulario() {
      try {
        axios.post('/api/user/', { nome: this.userName, game: this.jogoSelecionado })
          .then(response => {
            this.jogoSelecionado = '';
            this.userName = null;
            this.$emit('cadastroSucesso', 'Usuário');
          })
          .catch(error => {
            this.$emit('cadastroErro', 'Usuário');
          });
      } catch (error) {
        this.$emit('cadastroErro', 'Usuário');
      }
    },

  },
  created() {
    try {
      axios.get('/api/game/')
        .then(response => {
          response.data.forEach((element) => {
            this.jogos.push(element);
          });
        })
        .catch(error => {
          console.log(error);
        });
    } catch (error) {
      console.log(error);
    }
  }
};
</script>
  