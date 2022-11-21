#!/usr/bin/env nextflow

/*
==================================================================================
    	                        GenomOrder   Pipeline
==================================================================================
 GenomOrder Pipeline. Started January 2021.
 #### Authors ####
 Clément BIRBES <clement.birbes@inrae.fr>
*/

def helpMessage() {
    log.info"""
	=========================================
	 GenomOrder Pipeline v1.2
	=========================================
  Usage:
    The typical command for running the pipeline is as follows:
    nextflow run main.nf -profile {conda} --assembly [assemblyFile] --reference [referenceFile] [options]

    Mandatory arguments:
      --assembly          Path to assembly file (fa, fasta)
      --reference         Path to reference file (fa, fasta)

    Optionnal arguments:
      --assembly2       Path to second assembly file (fa, fasta)
      --assembly3       Path to third assembly file (fa, fasta)
      --assembly4       Path to fourth assembly file (fa, fasta)
      --assembly5       Path to fifth assembly file (fa, fasta)

      --arrange         If true, create DGenies backup and arrange assembly according to reference. If false, create DGenies backup (default, False)

      --compare         Run DGenie to compare target chromosome vs equivalent in others assembly. Input file with one chromosome name per row.
    """.stripIndent()
}

// Show help message
params.help = false
if (params.help){
    helpMessage()
    exit 0
}

params.filter2 = 'NO_FILE2'
params.filter3 = 'NO_FILE3'
params.filter4 = 'NO_FILE4'
params.filter5 = 'NO_FILE5'

if (!params.assembly || !params.reference) {
	exit 1, "You must specify both assembly and reference file using --assembly and --reference"
}
else {
  Assembly_ch = Channel.fromPath(params.assembly)
	    			         .ifEmpty {exit 1, "Assembly file not found: ${params.assembly}"}
                     .into {AssemblyMinimap_ch; AssemblyIndex_ch; AssemblyArrange_ch; AssemblyCompare_ch}
  Reference_ch = Channel.fromPath(params.reference)
                   	 .ifEmpty {exit 1, "Reference file not found: ${params.reference}"}
                     .into {ReferenceCompare_ch; ReferenceMinimap_ch; ReferenceIndex_ch; Reference2Minimap_ch; Reference2Index_ch; Reference3Minimap_ch; Reference3Index_ch; Reference4Minimap_ch; Reference4Index_ch; Reference5Minimap_ch; Reference5Index_ch}
}

if (params.assembly2){
  Assembly2_ch = Channel.fromPath(params.assembly2)
                .ifEmpty {exit 1, "Reference file not found: ${params.assembly2}"}
                .into {Assembly2Minimap_ch; Assembly2Index_ch; Assembly2Arrange_ch; Assembly2Compare_ch}
} else {
  Final2Assembly_ch = file(params.filter2)
  Assembly2Compare_ch = file(params.filter2)
  Alignment2Compare_ch = file('missing_All2')
}

if (params.assembly3){
  Assembly3_ch = Channel.fromPath(params.assembly3)
                .ifEmpty {exit 1, "Reference file not found: ${params.assembly3}"}
                .into {Assembly3Minimap_ch; Assembly3Index_ch; Assembly3Arrange_ch; Assembly3Compare_ch}
} else {
  Final3Assembly_ch = file(params.filter3)
  Assembly3Compare_ch = file(params.filter3)
  Alignment3Compare_ch = file('missing_All3')
}

if (params.assembly4){
  Assembly4_ch = Channel.fromPath(params.assembly4)
                .ifEmpty {exit 1, "Reference file not found: ${params.assembly4}"}
                .into {Assembly4Minimap_ch; Assembly4Index_ch; Assembly4Arrange_ch; Assembly4Compare_ch}
} else {
  Final4Assembly_ch = file(params.filter4)
  Assembly4Compare_ch = file(params.filter4)
  Alignment4Compare_ch = file('missing_All4')
 }

if (params.assembly5){
  Assembly5_ch = Channel.fromPath(params.assembly5)
                .ifEmpty {exit 1, "Reference file not found: ${params.assembly5}"}
                .into {Assembly5Minimap_ch; Assembly5Index_ch; Assembly5Arrange_ch; Assembly5Compare_ch}
} else {
  Final5Assembly_ch = file(params.filter5)
  Assembly5Compare_ch = file(params.filter5)
  Alignment5Compare_ch = file('missing_All5')
}

if (params.compare){
  Chromosome_ch = Channel.fromPath(params.compare)
                        .splitCsv()
                        .set{Chr_ch}
}

if (params.arrange){mode_arrange = true} else{mode_arrange = false}


// Boucle1 : Obligatoire, aligne assembly/ref, index assembly/ref et fait backup
process minimap {
  label 'process_high'

  input:
  file reference from ReferenceMinimap_ch
  file assembly from AssemblyMinimap_ch

  output:
  file 'alignment.paf' into AlignmentBackup_ch, AlignmentArrange_ch

  script:
  """
  minimap2 -t $task.cpus ${reference} ${assembly} > alignment.paf
  """
}

process index_files {
  label 'process_low'

  input:
  file reference from ReferenceIndex_ch
  file assembly from AssemblyIndex_ch

  output:
  file '*.idx' into IndexBackup_ch, IndexArrange_ch

  script:
  """
  index.py -i ${reference} -n ${reference.baseName} -o target.idx
  index.py -i ${assembly} -n ${assembly.baseName} -o query_${assembly.simpleName}.idx
  """
}

process create_backup {
  label 'process_low'
  publishDir = "${params.outdir}/Backup_assembly1"

  input:
  set file(query), file(target) from IndexBackup_ch
  file map from AlignmentBackup_ch

  output:
  file '*.tar' into tar_ch
  file 'map1.paf' into AlignmentCompare_ch

  script:
  """
  sort_paf.py -i ${map} -o map.paf
  mv query_*.idx query.idx
  tar -hcvf ${query.simpleName}.tar query.idx target.idx map.paf
  mv map.paf map1.paf
  """
}
// Boucle2 : Obligatoire, aligne assembly/ref, index assembly/ref et fait backup
if (params.assembly2){
  process minimap2 {
    label 'process_high'

    input:
    file reference from Reference2Minimap_ch
    file assembly from Assembly2Minimap_ch

    output:
    file 'alignment.paf' into Alignment2Backup_ch, Alignment2Arrange_ch

    script:
    """
    minimap2 -t $task.cpus ${reference} ${assembly} > alignment.paf
    """
  }

  process index_files2 {
    label 'process_low'

    input:
    file reference from Reference2Index_ch
    file assembly from Assembly2Index_ch

    output:
    file '*.idx' into Index2Backup_ch, Index2Arrange_ch

    script:
    """
    index.py -i ${reference} -n ${reference.baseName} -o target.idx
    index.py -i ${assembly} -n ${assembly.baseName} -o query_${assembly.simpleName}.idx
    """
  }

  process create_backup2 {
    label 'process_low'
    publishDir = "${params.outdir}/Backup_assembly2"

    input:
    set file(query), file(target) from Index2Backup_ch
    file map from Alignment2Backup_ch

    output:
    file '*.tar' into tar2_ch
    file 'map2.paf' into Alignment2Compare_ch

    script:
    """
    sort_paf.py -i ${map} -o map.paf
    mv query_*.idx query.idx
    tar -hcvf ${query.simpleName}.tar query.idx target.idx map.paf
    mv map.paf map2.paf
    """
  }
}

// Boucle3 : Obligatoire, aligne assembly/ref, index assembly/ref et fait backup
if (params.assembly3){
  process minimap3 {
    label 'process_high'

    input:
    file reference from Reference3Minimap_ch
    file assembly from Assembly3Minimap_ch

    output:
    file 'alignment.paf' into Alignment3Backup_ch, Alignment3Arrange_ch

    script:
    """
    minimap2 -t $task.cpus ${reference} ${assembly} > alignment.paf
    """
  }

  process index_files3 {
    label 'process_low'

    input:
    file reference from Reference3Index_ch
    file assembly from Assembly3Index_ch

    output:
    file '*.idx' into Index3Backup_ch, Index3Arrange_ch

    script:
    """
    index.py -i ${reference} -n ${reference.baseName} -o target.idx
    index.py -i ${assembly} -n ${assembly.baseName} -o query_${assembly.simpleName}.idx
    """
  }

  process create_backup3 {
    label 'process_low'
    publishDir = "${params.outdir}/Backup_assembly3"

    input:
    set file(query), file(target) from Index3Backup_ch
    file map from Alignment3Backup_ch

    output:
    file '*.tar' into tar3_ch
    file 'map3.paf' into Alignment3Compare_ch

    script:
    """
    sort_paf.py -i ${map} -o map.paf
    mv query_*.idx query.idx
    tar -hcvf ${query.simpleName}.tar query.idx target.idx map.paf
    mv map.paf map3.paf
    """
  }
}

// Boucle4 : Obligatoire, aligne assembly/ref, index assembly/ref et fait backup
if (params.assembly4){
  process minimap4 {
    label 'process_high'

    input:
    file reference from Reference4Minimap_ch
    file assembly from Assembly4Minimap_ch

    output:
    file 'alignment.paf' into Alignment4Backup_ch, Alignment4Arrange_ch

    script:
    """
    minimap2 -t $task.cpus ${reference} ${assembly} > alignment.paf
    """
  }

  process index_files4 {
    label 'process_low'

    input:
    file reference from Reference4Index_ch
    file assembly from Assembly4Index_ch

    output:
    file '*.idx' into Index4Backup_ch, Index4Arrange_ch

    script:
    """
    index.py -i ${reference} -n ${reference.baseName} -o target.idx
    index.py -i ${assembly} -n ${assembly.baseName} -o query_${assembly.simpleName}.idx
    """
  }

  process create_backup4 {
    label 'process_low'
    publishDir = "${params.outdir}/Backup_assembly4"

    input:
    set file(query), file(target) from Index4Backup_ch
    file map from Alignment4Backup_ch

    output:
    file '*.tar' into tar4_ch
    file 'map4.paf' into Alignment4Compare_ch

    script:
    """
    sort_paf.py -i ${map} -o map.paf
    mv query_*.idx query.idx
    tar -hcvf ${query.simpleName}.tar query.idx target.idx map.paf
    mv map.paf map4.paf
    """
  }
}

// Boucle5 : Obligatoire, aligne assembly/ref, index assembly/ref et fait backup
if (params.assembly5){
  process minimap5 {
    label 'process_high'

    input:
    file reference from Reference5Minimap_ch
    file assembly from Assembly5Minimap_ch

    output:
    file 'alignment.paf' into Alignment5Backup_ch, Alignment5Arrange_ch

    script:
    """
    minimap2 -t $task.cpus ${reference} ${assembly} > alignment.paf
    """
  }

  process index_files5 {
    label 'process_low'

    input:
    file reference from Reference5Index_ch
    file assembly from Assembly5Index_ch

    output:
    file '*.idx' into Index5Backup_ch, Index5Arrange_ch

    script:
    """
    index.py -i ${reference} -n ${reference.baseName} -o target.idx
    index.py -i ${assembly} -n ${assembly.baseName} -o query_${assembly.simpleName}.idx
    """
  }

  process create_backup5 {
    label 'process_low'
    publishDir = "${params.outdir}/Backup_assembly5"

    input:
    set file(query), file(target) from Index5Backup_ch
    file map from Alignment5Backup_ch

    output:
    file '*.tar' into tar5_ch
    file 'map5.paf' into Alignment5Compare_ch

    script:
    """
    sort_paf.py -i ${map} -o map.paf
    mv query_*.idx query.idx
    tar -hcvf ${query.simpleName}.tar query.idx target.idx map.paf
    mv map.paf map5.paf
    """
  }
}

// Boucle Arrange : Optionnel, reorganise l'assemblage
if (params.arrange){
  process arrange_assembly {
    label 'process_low'
    publishDir = "${params.outdir}/Arranged_assembly"

    input:
    set file(query), file(target) from IndexArrange_ch
    file map from AlignmentArrange_ch
    file fasta from AssemblyArrange_ch

    output:
    file 'As_ref_*' into FinalAssembly_ch

    script:
    """
    Arrange.py --paf ${map} --queryIdx ${query} --refIdx ${target} --inputFasta ${fasta}
    """
  }

  if (params.assembly2){
    process arrange_assembly2 {
      label 'process_low'
      publishDir = "${params.outdir}/Arranged_assembly2"

      input:
      set file(query), file(target) from Index2Arrange_ch
      file map from Alignment2Arrange_ch
      file fasta from Assembly2Arrange_ch

      output:
      file 'As_ref_*' into Final2Assembly_ch

      script:
      """
      Arrange.py --paf ${map} --queryIdx ${query} --refIdx ${target} --inputFasta ${fasta}
      """
    }
  }

  if (params.assembly3){
    process arrange_assembly3 {
      label 'process_low'
      publishDir = "${params.outdir}/Arranged_assembly3"

      input:
      set file(query), file(target) from Index3Arrange_ch
      file map from Alignment3Arrange_ch
      file fasta from Assembly3Arrange_ch

      output:
      file 'As_ref_*' into Final3Assembly_ch

      script:
      """
      Arrange.py --paf ${map} --queryIdx ${query} --refIdx ${target} --inputFasta ${fasta}
      """
    }
  }

  if (params.assembly4){
    process arrange_assembly4 {
      label 'process_low'
      publishDir = "${params.outdir}/Arranged_assembly4"

      input:
      set file(query), file(target) from Index4Arrange_ch
      file map from Alignment4Arrange_ch
      file fasta from Assembly4Arrange_ch

      output:
      file 'As_ref_*' into Final4Assembly_ch

      script:
      """
      Arrange.py --paf ${map} --queryIdx ${query} --refIdx ${target} --inputFasta ${fasta}
      """
    }
  }

  if (params.assembly5){
    process arrange_assembly5 {
      label 'process_low'
      publishDir = "${params.outdir}/Arranged_assembly5"

      input:
      set file(query), file(target) from Index5Arrange_ch
      file map from Alignment5Arrange_ch
      file fasta from Assembly5Arrange_ch

      output:
      file 'As_ref_*' into Final5Assembly_ch

      script:
      """
      Arrange.py --paf ${map} --queryIdx ${query} --refIdx ${target} --inputFasta ${fasta}
      """
    }
  }
}

// Boucle Compare : Optionnel, focus sur les chromosome cible
if (params.compare){
// Si l'assemblage a déjà été réorganisé
  if (mode_arrange){
    process compare_assembly {
      label 'process_high'
      publishDir = "${params.outdir}/Compared_assembly"

      input:
      each chrName from Chr_ch.flatten()
      file reference from ReferenceCompare_ch
      file assembly1 from FinalAssembly_ch
      file assembly2 from Final2Assembly_ch
      file assembly3 from Final3Assembly_ch
      file assembly4 from Final4Assembly_ch
      file assembly5 from Final5Assembly_ch

      output:
      file '*.tar' into ComparedAssembly_ch

      script:
      """
      CreateChrFasta.py --Chr ${chrName} --Ref ${reference} --assembly1 ${assembly1} --assembly2 ${assembly2} --assembly3 ${assembly3} --assembly4 ${assembly4} --assembly5 ${assembly5}

      minimap2 -t $task.cpus -X ${chrName}File.fasta ${chrName}File.fasta > alignment.paf

      index.py -i ${chrName}File.fasta -n reference -o target.idx
      cp target.idx query.idx

      sort_paf.py -i alignment.paf -o mapIn.paf
      InversePaf.py
      tar -hcvf ${chrName}.tar target.idx query.idx map.paf
      """
    }
  }
  else{
// Si l'assemblage n'a pas été réorganisé
    process compare__assembly {
      label 'process_high'
      publishDir = "${params.outdir}/Compared_assembly"

      input:
      each chrName from Chr_ch.flatten()
      file reference from ReferenceCompare_ch
      file assembly1 from AssemblyCompare_ch
      file alignment1 from AlignmentCompare_ch
      file assembly2 from Assembly2Compare_ch
      file alignment2 from Alignment2Compare_ch
      file assembly3 from Assembly3Compare_ch
      file alignment3 from Alignment3Compare_ch
      file assembly4 from Assembly4Compare_ch
      file alignment4 from Alignment4Compare_ch
      file assembly5 from Assembly5Compare_ch
      file alignment5 from Alignment5Compare_ch

      output:
      file '*.tar' into ComparedAssembly_ch

      script:
      """
      renameChr.py --Chr ${chrName} --Ref ${reference} --Assembly1 ${assembly1} --Assembly2 ${assembly2} --Assembly3 ${assembly3} --Assembly4 ${assembly4} --Assembly5 ${assembly5}

      minimap2 -t $task.cpus -X ${chrName}File.fasta ${chrName}File.fasta > alignment.paf

      index.py -i ${chrName}File.fasta -n reference -o target.idx
      cp target.idx query.idx

      sort_paf.py -i alignment.paf -o mapIn.paf
      InversePaf.py
      tar -hcvf ${chrName}.tar target.idx query.idx map.paf
      """
    }
  }
}
