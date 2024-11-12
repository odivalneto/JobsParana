function generateBreadcrumbs() {
    const breadcrumbsContainer = document.getElementById("breadcrumbs");
    const urlSegments = window.location.pathname.split('/').filter(segment => segment);

    let breadcrumbsHTML = '<a href="/">Início</a>';
    let path = '';

    urlSegments.forEach((segment, index) => {
        path += `/${segment}`;
        const isLastSegment = index === urlSegments.length - 1;

        if (isLastSegment) {
            breadcrumbsHTML += ` <span> &gt; </span> <span>${decodeURIComponent(segment)}</span>`;
        } else {
            breadcrumbsHTML += ` <span> &gt; </span> <a href="${path}">${decodeURIComponent(segment)}</a>`;
        }
    });

    breadcrumbsContainer.innerHTML = breadcrumbsHTML;
}