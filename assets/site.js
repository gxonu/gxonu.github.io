const toggle=document.querySelector('.xp-toggle');
if(toggle)toggle.addEventListener('click',()=>{
  const open=document.getElementById('xpCard').classList.toggle('open');
  toggle.setAttribute('aria-expanded',String(open));
  document.getElementById('xpLabel').textContent=open?'Hide details':'Show details';
});
