<template>
  <div class="m-3">
    <h1>
      Projeto desenvolvido para defesa do TCC.
    </h1>
    <div class="rounded p-3 cards">
      <h3>Como funciona?</h3>
      <div class="ms-3">
        <p>1º: Na aba Cadastro, efetue o registro de seu Jogo.</p>
        <p>2º: Na aba Cadastro, efetue o registro dos artefatos que serão monitorados (ex: Tempo de fase, Respostas de
          perguntas, etc...)</p>
        <p>3º: Utilize o endpoint /api/data/ para enviar os dados.</p>
        <p>4º: Na aba Dashboard selecione as informações para gerar os gráficos.</p>
      </div>
      <h4>Dicas!</h4>
      <div class="ms-3">
        <p>Ao gerar o Dashboard é possível selecionar mais de um artefato para exibir as informações.</p>
        <p>É possível identificar a origem da informação por meio do campo "id" dos dados (ex: um usuário, uma instância,
          etc...).</p>
      </div>
    </div>
    <div class="rounded p-3 mt-3 cards">
      <h3>
        APIs
      </h3>
      <div class="ms-3">
        <h4 v-for="api in apis">
          {{ api.nome }}
          <ul>
            <li v-for="campo in api.campos">
              {{ campo }}
            </li>
          </ul>
        </h4>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      apis: [
        {
          nome: 'Jogo (/api/game/)',
          campos: [
            'sequence: smallint (auto)',
            'nome: String'
          ]
        },
        {
          nome: 'Artefato (/api/artifact/)',
          campos: [
            'sequence: smallint (auto)',
            'id: string',
            'nome: string',
            'game: smallint',
            'type: string (numeric, timestamp (seconds), interval (seconds), text, bool)'
          ]
        },
        {
          nome: 'Dados (/api/data/)',
          campos: [
            'sequence: bigint (auto)',
            'game: smallint',
            'id: text (opcional)',
            'artifact: string',
            'value: string'
          ]
        },
      ]
    };
  },
}
</script>
<style></style>
