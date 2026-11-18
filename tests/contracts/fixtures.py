from uistandards.core import COMMIT, FILES, load_baseline


def request():
    return {'contract_version':'1.0.0','skill':'ui-audit','mode':'audit',
        'baseline':{'repository':'ui-standards','commit':COMMIT,'version':'G1-0.1.1','hashes':{k:FILES[k][1] for k in ('spec','matrix_derived','scenarios')}},
        'target':{'project':'fixture','repository':'fixture','revision':'fixture','scope':'fixture','flows':['fixture']},
        'environment':{'os':'linux','agent':'fixture','agent_version':'1','browser':None,'device':None,'viewport':None,'zoom':None},
        'authorization':{'reference':'fixture-read-only','operations':['read'],'writable_paths':[],'methods':['S']},
        'output':{'delivery':'inline','path':None},'task':'fixture','environment_limitations':['UI não observada']}


def result(root, req):
    rules=load_baseline(root)
    return {'contract_version':'1.0.0','result_version':'1.0.0','run_id':'a06872fa-6850-44b4-baba-4c5a238526a2','skill':req['skill'],'mode':req['mode'],
        'execution_state':'PARCIAL','started_at':'2026-11-18T12:00:00Z','finished_at':'2026-11-18T12:01:00Z','executor':'fixture','request_ref':'0'*64,
        'baseline':{**req['baseline'],'repository_integrity':'VERIFICADA','source_provenance':'NAO_VERIFICADA','approval_state':'HOMOLOGADA_COM_RESSALVAS','approval_reference':'registro aditivo'},
        'target':req['target'],'environment':req['environment'],'scope':req['target']['scope'],'authorization_ref':req['authorization']['reference'],
        'rules':[{'id':rid,'scenario_id':r['scenario_id'],'applicability':'INDETERMINADA','required_methods':r['methods'],'method_results':[],'status':'NAO_VERIFICADO','exceptions':[],'limitations':['fora do escopo']} for rid,r in rules.items()],
        'findings':[],'evidence':[],'limitations':['Proveniência não verificada'],'errors':[],'artifacts':[],'changed_files':[]}
