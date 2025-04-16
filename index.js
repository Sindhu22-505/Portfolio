// Toggle visibility for About section
document.querySelector('#about a').addEventListener('click', function (e) {
    e.preventDefault();
    const aboutDetails = document.querySelector('#about p');
    aboutDetails.style.display = aboutDetails.style.display === 'none' ? 'block' : 'none';
  });
  
  // Toggle visibility for Education section
  document.querySelector('#education a').addEventListener('click', function (e) {
    e.preventDefault();
    const educationDetails = document.querySelector('#education ul');
    educationDetails.style.display = educationDetails.style.display === 'none' ? 'block' : 'none';
  });
  
  // Toggle visibility for Skills section
  document.querySelector('#skills a').addEventListener('click', function (e) {
    e.preventDefault();
    const skillsList = document.querySelector('#skills ul');
    skillsList.style.display = skillsList.style.display === 'none' ? 'block' : 'none';
  });
  
  // Toggle visibility for Contact section
  document.querySelector('#contact a').addEventListener('click', function (e) {
    e.preventDefault();
    const contactDetails = document.querySelectorAll('#contact p');
    contactDetails.forEach(p => {
      p.style.display = p.style.display === 'none' ? 'block' : 'none';
    });
  });
  